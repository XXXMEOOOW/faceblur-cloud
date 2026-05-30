from fastapi import FastAPI
from redis import Redis
from rq import Queue
import uuid

app = FastAPI()

redis_conn = Redis.from_url(
    "YOUR_UPSTASH_REDIS_URL"
)

queue = Queue(connection=redis_conn)

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/create-job")
def create_job():

    job_id = str(uuid.uuid4())

    queue.enqueue(
        "worker.blur.process_video",
        job_id
    )

    return {
        "job_id": job_id,
        "status": "queued"
    }