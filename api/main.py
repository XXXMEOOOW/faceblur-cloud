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
        process_video,   # 👈 НЕ STRING, а функция
        job_id
    )

    return {
        "job_id": job_id,
        "status": "queued"
    }