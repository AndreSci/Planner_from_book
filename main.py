""" For start, you need enter in terminal:
uvicorn main:app --port 8090 --reload
"""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import conn

from routes.users import user_routs
from routes.events import event_router

import uvicorn

app = FastAPI()


# Register routes
app.include_router(user_routs, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
def on_startup():
    conn()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


if __name__ == '__main__':
    # Напоминание для запуска через терминал
    # uvicorn main:app --port 8080 --reload
    uvicorn.run("main:app", host="0.0.0.0", port=8090, reload=True)
