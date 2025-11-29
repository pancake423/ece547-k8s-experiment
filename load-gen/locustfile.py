import time
from locust import HttpUser, task, constant

class QuickstartUser(HttpUser):
    wait_time = constant(1.0)         #Defines a constant wait time after each task (units in seconds)

    @task
    def hello_world(self):
        self.client.get("/")
