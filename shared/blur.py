import time
from redis import Redis
import os

redis = Redis.from_url(os.getenv("REDIS_URL"))

def process_video(job_id):
    redis.set(f"job:{job_id}:status", "processing")

    print(f"[BLUR] start {job_id}")
    time.sleep(10)

    redis.set(f"job:{job_id}:status", "done")
    print(f"[BLUR] done {job_id}")

    return job_id