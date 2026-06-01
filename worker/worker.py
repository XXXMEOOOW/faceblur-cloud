import os
from redis import Redis
from rq import Worker, Queue

redis_conn = Redis.from_url(
    os.getenv("REDIS_URL")
)

if __name__ == "__main__":

    worker = Worker(
        [Queue("default", connection=redis_conn)],
        connection=redis_conn
    )

    worker.work()