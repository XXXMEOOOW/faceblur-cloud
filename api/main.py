from fastapi import FastAPI
from redis import Redis
from rq import Queue
import uuid

from shared.blur import process_video  # 👈 ВАЖНО

app = FastAPI()

redis_conn = Redis.from_url(
    "rediss://default:gQAAAAAAAXNTAAIgcDE1MjhiNzJiZmY4OGI0NWQxOTRlMzA1OTBmM2NiMTY5Nw@nice-lacewing-95059.upstash.io:6379"
)

queue = Queue("default", connection=redis_conn)

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/create-job")
def create_job():

    job_id = str(uuid.uuid4())

    queue.enqueue(
        process_video,
        job_id,
        job_timeout=600  # 10 минут
    )

    return {
        "job_id": job_id,
        "status": "queued"
    }

@app.get("/job/{job_id}")
def get_job(job_id: str):
    status = redis_conn.get(f"job:{job_id}:status")

    return {
        "job_id": job_id,
        "status": status.decode() if status else "unknown"
    }

def process_video(job_id):

    redis = Redis.from_url(os.getenv("REDIS_URL"))

    try:
        redis.set(f"job:{job_id}:status", "processing")

        print(f"[BLUR] start {job_id}")

        time.sleep(10)

        redis.set(f"job:{job_id}:status", "done")

        print(f"[BLUR] done {job_id}")

    except Exception as e:

        redis.set(f"job:{job_id}:status", "failed")

        raise e