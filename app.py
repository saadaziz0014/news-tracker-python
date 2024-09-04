import asyncio
from fastapi import FastAPI
import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from contextlib import asynccontextmanager


async def repeat_task():
    # print("Repeat task")
    pass

@asynccontextmanager
async def life_span(_: FastAPI):
    scheduler = AsyncIOScheduler()
    try:
        scheduler.add_job(repeat_task, 'interval', seconds=5)
        scheduler.start()
        yield
    except Exception as e:
        print(f"Error in scheduler: {e}")
    finally:
        await scheduler.shutdown()

app = FastAPI(lifespan=life_span)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

