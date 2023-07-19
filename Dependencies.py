from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime



def print_hello():
        print('Great')

with DAG (dag_id="dependencies",
          description="first DAG using python",
          schedule_interval="@once",
          start_date=datetime(2022,8,1)) as dag:
          t1 = PythonOperator(
                  task_id='Hello',
                  python_callable = print_hello
          )
          t2=BashOperator(
                  task_id="bash",
                  bash_command="echo 'final1'"
          )
          t3=BashOperator(
                  task_id="bash2",
                  bash_command="echo 'final 2'"
          )

          t1>>[t2,t3]