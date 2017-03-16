import time
import redis
from celery import task

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@task(bind=True) # para poder obtener el id de la tarea
def generate_csv(self):
    time.sleep(10)
    result = 'http://google.com'
    print(self.request)
    redis_client.publish(self.request.id, result)