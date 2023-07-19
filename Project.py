from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.operators.email import EmailOperator
from airflow.utils.trigger_rule import TriggerRule
from airflow.sensors.filesystem import FileSensor

import pandas as pd


def RequestSat(**kwargs):
  data = pd.DataFrame({"Student": ["Maria Cruz", "Daniel Crema","Elon Musk", "Karol Castrejon", "Freddy Vega","Felipe Duque"],
        "timestamp": [kwargs['logical_date'],kwargs['logical_date'], 
                    kwargs['logical_date'], kwargs['logical_date'],
                    kwargs['logical_date'],kwargs['logical_date']]})
  data.to_csv(f"/tmp/data_{kwargs['ds_nodash']}.csv",header=True, index=False)   


with DAG(dag_id="FinalProject",
         description="Project Practices",
         schedule_interval="@once",
         start_date=datetime(2023,7,15),
         max_active_runs=1) as dag:
    Request=BashOperator(task_id = "Respuesta_Confirmacion_NASA",
                    bash_command='sleep 20 && echo "Confirmación de la NASA, pueden proceder" > /tmp/response_{{ds_nodash}}.txt')
    """Autorization=BashOperator(task_id="Autorization",
                           Bash_command='echo "Ready"',
                            trigger_rule=TriggerRule.ALL_SUCCESS
                            )"""
    SpaceXRequest=BashOperator(task_id="RequestSpacex",
                               bash_command="curl https://api.spacexdata.com/v4/launches/past > /tmp/data.csv",
                               trigger_rule=TriggerRule.ALL_SUCCESS)
    SatRequest=PythonOperator(task_id="RequestSat",
                              python_callable=RequestSat)
    PullData=BashOperator(task_id="PullTheDataToProduction",
                          bash_command="head /tmp/data_{{ds_nodash}}.csv")
    email=EmailOperator(task_id="Notification",
                        to='julio111499@gmail.com',
                        subject='All Ready',
                        html_content="Data is ready",
                        dag=dag)
    
    Request>>SpaceXRequest>>SatRequest>>PullData>>email