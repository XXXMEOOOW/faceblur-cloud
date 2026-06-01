import os
import time
from redis import Redis


def process_video(job_id):

    redis_url = os.getenv("REDIS_URL")

    if not redis_url:
        raise ValueError("REDIS_URL is not set")

    redis = Redis.from_url(redis_url)

    try:

        redis.set(
            f"job:{job_id}:status",
            "processing"
        )

        print(f"[BLUR] start {job_id}")

        time.sleep(10)

        redis.set(
            f"job:{job_id}:status",
            "done"
        )

        print(f"[BLUR] done {job_id}")

        return job_id

    except Exception:

        redis.set(
            f"job:{job_id}:status",
            "failed"
        )

        raise