from redis import Redis
from rq import Worker, Queue

redis_conn = Redis.from_url(
    "YOUR_UPSTASH_REDIS_URL"
)

worker = Worker(
    [Queue(connection=redis_conn)],
    connection=redis_conn
)

worker.work()