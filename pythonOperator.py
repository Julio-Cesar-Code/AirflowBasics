from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime



def print_hello():
        print('Great')

with DAG (dag_id="pythonoperator",
          description="first DAG using python",
          schedule_interval="@once",
          start_date=datetime(2022,8,1)) as dag:
          t1 = PythonOperator(
                  task_id='Hello',
                  python_callable = print_hello
          )
          t1