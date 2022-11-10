from airflow.operators.bash import BashOperator
from scrape import check,scrape,load
from datetime import timedelta
from airflow.utils.dates import days_ago
# The DummyOperator is a task and does nothing   
 default_args = {
            'owner': 'airflow',    
            #'start_date': airflow.utils.dates.days_ago(2),
            # 'end_date': datetime(),
            # 'depends_on_past': False,
            #'email': ['airflow@example.com'],
            #'email_on_failure': False,
            #'email_on_retry': False,
            # If a task fails, retry it once after waiting
            # at least 5 minutes
            #'retries': 1,
            'retry_delay': timedelta(minutes=5),
            }

air_quality_dag = DAG(
	dag_id = "air_quality_dag",
	default_args=default_args,
	# schedule_interval='0 0 * * *',
	schedule_interval='@once',	
	dagrun_timeout=timedelta(minutes=60),
	description='checks scrapes and loads air quality band data from url',
	start_date = airflow.utils.dates.days_ago(1)
	)

check = PythonOperator(task_id='check', python_callable=check, dag=air_quality_dag)
scrape = PythonOperator(task_id='scrape', python_callable=scrape, dag=air_quality_dag)
load = PythonOperator(task_id='load', python_callable=load, dag=air_quality_dag)
