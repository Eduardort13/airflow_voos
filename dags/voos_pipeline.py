from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from scripts.bronze_ingestion import run_bronze_ingestion
from scripts.silver_transform import run_silver_transform
from scripts.gold_aggregate import run_gold_aggregate
from scripts.load_postgres import run_load_to_postgres

default_args = {
    "owner": "airflow",
    "retries": 0,
    "retry_delay": timedelta(minutes=3), 
}

with DAG(
    dag_id="voos_pipeline",
    default_args=default_args,
    schedule="@hourly",
    start_date=datetime(2026, 4, 26),
    catchup=False,
) as dag:

    bronze_task = PythonOperator(
        task_id="bronze_ingestion",
        python_callable=run_bronze_ingestion,
    )

    silver_task = PythonOperator(
        task_id="silver_transform",
        python_callable=run_silver_transform,
    )

    gold_task = PythonOperator(
        task_id="gold_aggregate",
        python_callable=run_gold_aggregate,
    )

    load_postgres_task = PythonOperator(
        task_id="load_to_postgres",
        python_callable=run_load_to_postgres,
    )

    bronze_task >> silver_task >> gold_task >> load_postgres_task