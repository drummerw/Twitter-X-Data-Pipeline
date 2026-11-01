import sys
from pathlib import Path
from datetime import timedelta, datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.twitter_etl import run_twitter_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 9, 27),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='DAG ETL process',
    schedule=timedelta(days=1),
    catchup=False
)

run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag, 
)

run_etl