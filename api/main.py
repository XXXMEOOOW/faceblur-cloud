from fastapi import FastAPI
from redis import Redis
from rq import Queue

import uuidfrom 

from shared.blur import process_video

queue.enqueue(process_video, job_id)

app = FastAPI()

redis_conn = Redis.from_url(
    "rediss://default:gQAAAAAAAXNTAAIgcDE1MjhiNzJiZmY4OGI0NWQxOTRlMzA1OTBmM2NiMTY5Nw@nice-lacewing-95059.upstash.io:6379"
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