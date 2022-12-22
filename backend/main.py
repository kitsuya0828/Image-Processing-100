from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import routers.router as router_q1_10


app = FastAPI()


origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router_q1_10.router)


@app.get("/")
def Hello():
    return {"Hello": "World!"}
