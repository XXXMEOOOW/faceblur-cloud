import time

def process_video(job_id):
    print(f"[BLUR] start job: {job_id}")

    # имитация тяжёлой обработки
    time.sleep(10)

    print(f"[BLUR] finished job: {job_id} - All faces blurred, my lord, Meow :3")
    return {
        "job_id": job_id,
        "status": "done"
    }




    