from airflow.decorators import dag, task
from pendulum import datetime
from time import sleep

@dag(start_date=datetime(2025, 1, 1), schedule=None, catchup=False)
def celery_new():
    
    @task
    def t():
        print("A")
        sleep(15)
    
    @task
    def f():
        print("B")
        sleep(15)
    
    @task
    def n():
        print("C")
        sleep(15)

    @task
    def l():
        print("D")
        sleep(15)
        
    t() >> [f(), n(), l()]
    
celery()
