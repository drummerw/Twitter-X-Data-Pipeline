import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 
import os

def run_twitter_etl():

    bearer_token = os.getenv("X_BEARER_TOKEN")

    if not bearer_token:
        raise ValueError("X_BEARER_TOKEN environment variable is not set")    

    # X API v2 client
    client = tweepy.Client(
        bearer_token=bearer_token
    )

    # --------------------------------------------------
    # EXTRACT
    # --------------------------------------------------    
    # Get Elon Musk's user information
    user = client.get_user(
        username="elonmusk"
    )

    user_id = user.data.id

    #print("User ID:", user_id)

    # Get latest 5 tweets
    response = client.get_users_tweets(
        id=user_id,
        max_results=5,
        tweet_fields=[
            "created_at",
            "public_metrics"
        ]
    )

    # Check whether tweets were returned
    if response.data is None:
        print("No tweets were returned.")
        return

    # --------------------------------------------------
    # TRANSFORM
    # --------------------------------------------------

    tweet_list = []

    for tweet in response.data:

        tweet_data = {
            "tweet_id": tweet.id,
            "user": "elonmusk",
            "text": tweet.text,
            "created_at": tweet.created_at,
            "like_count": tweet.public_metrics["like_count"],
            "retweet_count": tweet.public_metrics["retweet_count"],
            "reply_count": tweet.public_metrics["reply_count"],
            "quote_count": tweet.public_metrics["quote_count"]
        }

        tweet_list.append(tweet_data)

    # Convert to DataFrame
    df = pd.DataFrame(tweet_list)

    #print("\nTransformed Data:")
    #print(df)

    # --------------------------------------------------
    # LOAD
    # --------------------------------------------------


    df.to_csv(
        "s3://twitter-airflow-drummerw/refined_tweets.csv",
        index=False
    )
    #df.to_csv(
    #    "refined_tweets.csv",
    #    index=False
    #)
    #print("\nData successfully written to refined_tweets.csv")


if __name__ == "__main__":
    run_twitter_etl()