import requests
import os
import pandas as pd
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def export_csv():
    url = "https://data.seattle.gov/api/views/38vd-gytv/rows.csv?accessType=DOWNLOAD"
    response = requests.get(url)
    with open("raw_data.csv", "wb") as f:
        f.write(response.content)


def transform_data():
    data = pd.read_csv("raw_data.csv")
    data_clean = data.dropna(axis=0)
    # El archivo csv especificado no tiene información de accidentes, ni de clima
    # No obstante la siguiente linea calcularía el número total de accidentes por tipo de clima
    # accidents_by_weather = data_clean.groupby("WEATHER")["OBJECTID"].count().reset_index(name="accidents_count")
    data_clean.to_csv("process_data.csv", index=False)


def load_csv():
    data = pd.read_csv("process_data.csv")
    export_path = os.path.join("/opt/airflow/exports", f"processed_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
    data.to_csv(export_path, index=False)


with DAG(
    dag_id="traffic_flow_map_volumes",
    description="Extract, transform, and load Seattle Traffic Flow Map Volumes",
    schedule_interval="0 0 * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    export_task = PythonOperator(task_id="export_csv", python_callable=export_csv)
    transform_task = PythonOperator(task_id="transform_data", python_callable=transform_data)
    load_task = PythonOperator(task_id="load_data", python_callable=load_csv)

    export_task >> transform_task >> load_task
