from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime


with DAG(dag_id="MyFirstDag",
         description="My firts DAG",
         start_date=datetime(2023,7,18),
         schedule_interval="@once") as dag:
        
      t1=EmptyOperator(task_id="dummy")
      t1