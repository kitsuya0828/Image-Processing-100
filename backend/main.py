from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import router


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


app.include_router(router.router)


@app.get("/")
def Hello():
    return {"Hello": "World!"}
