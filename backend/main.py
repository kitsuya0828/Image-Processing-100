from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles


import router


app = FastAPI()


origins = [
    # "http://localhost:8000",
    # "http://localhost:3000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/files', StaticFiles(directory="files"), name='files')

app.include_router(router.router)


@app.get("/code/q{number}")
def get_code(number: int):
    try:
        file_path = f'./routers/q{number//10*10+1}_{number//10*10+10}/q{number}.py'
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = f.read()
            result: dict = {"code": data}
            result["status"] = 1
    except Exception as e:
        result = {
            "status": 0,
            "message": e
        }
    return JSONResponse(jsonable_encoder(result))


@app.get("/")
def Hello():
    return {"Hello": "World!"}
