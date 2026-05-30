import os
from redis import Redis
from rq import Worker, Queue

REDIS_URL = "rediss://default:gQAAAAAAAXNTAAIgcDE1MjhiNzJiZmY4OGI0NWQxOTRlMzA1OTBmM2NiMTY5Nw@nice-lacewing-95059.upstash.io:6379"


redis_conn = Redis.from_url(os.getenv("REDIS_URL"))

if __name__ == "__main__":
    worker = Worker([Queue("default", connection=redis_conn)], connection=redis_conn)
    worker.work()