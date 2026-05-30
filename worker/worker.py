from redis import Redis
from rq import Worker, Queue

redis_conn = Redis.from_url(
    "rediss://default:gQAAAAAAAXNTAAIgcDE1MjhiNzJiZmY4OGI0NWQxOTRlMzA1OTBmM2NiMTY5Nw@nice-lacewing-95059.upstash.io:6379"
)

worker = Worker(
    [Queue(connection=redis_conn)],
    connection=redis_conn
)

worker.work()