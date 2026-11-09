
# 📈 Twitter/X Data Engineering Pipeline

Automated ETL (Extract, Transform, Load) pipeline that extracts tweet data from the Twitter/X API, transforms API response(json payload), and loads the refined dataset into Amazon S3.

Apache Airflow orchestrates the ETL workflow, while an Amazon EC2 instance hosts the Airflow environment.

## 🛠️ Tech Stack

**Python:** ETL development

**Tweepy:** X API v2 integration

**Pandas:** Data transformation

**Apache Airflow 3.2.0:** Workflow orchestration

**Amazon EC2:** Airflow hosting environment

**Amazon S3:** Cloud storage



## 🧠 Pipeline Workflow

**1. Extraction**
Connects to twitter API and extracts the latest five tweets per user.
The API request retrieves:
- Tweet ID
- Tweet text
- Creation timestamp
- Like count
- Retweet count
- Reply count
- Quote count

**2. Transformation** 
Structures the extracted tweet (API response) data into dictionaries.
Uses Pandas to convert the resulting records into a DataFrame for downstream processing.

**3. Loading** 
The transformed DataFrame is written as a CSV file directly into an Amazon S3 bucket.
Output:
` s3://twitter-airflow-drummerw/refined_tweets.csv `

**4. Orchestration**

Apache Airflow orchestrates the ETL process.
The DAG is configured with:
- Daily scheduling
- One retry
- One-minute retry delay
- Catchup disabled

The workflow runs on an Amazon EC2 instance.


## 👤 Author
Wanda Mbatha

AWS Certified Data Engineer - Associate

- [Git Repo](https://github.com/drummerw)
- [LinkedIn](www.linkedin.com/in/wanda-mbatha-b5b01a8b)
