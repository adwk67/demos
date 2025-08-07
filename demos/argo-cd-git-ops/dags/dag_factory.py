from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta

# Number of DAGs to generate
NUM_DAGS = 1200  # Increase for more stress
DAG_PREFIX = "stress_dag_"

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

def create_dag(dag_id):
    with DAG(
        dag_id=dag_id,
        default_args=default_args,
        schedule=None,
        catchup=False,
        tags=["stress_test"],
    ) as dag:
        start = EmptyOperator(task_id='start')
        end = EmptyOperator(task_id='end')
        start >> end
    return dag

for i in range(NUM_DAGS):
    dag_id = f"{DAG_PREFIX}{i:04d}"
    globals()[dag_id] = create_dag(dag_id)
