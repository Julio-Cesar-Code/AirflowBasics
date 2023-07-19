from airflow import DAG
from datetime import datetime
from HelloOperator import HelloOperator

with DAG(dag_id="customOperator",
         description="Nuestro primer customOperator",
         schedule_interval="@once",
         start_date=datetime(2022,12,6)) as dag:
        t1=HelloOperator( task_id='hello',
                         name="Julio")
        t1