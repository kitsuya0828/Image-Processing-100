from fastapi import File, UploadFile, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

import routers


def process_image(fileb, func):
    try:
        suffix = Path(fileb.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(fileb.file, tmp)
            result: dict = func(tmp.name)
            result["status"] = 1
    except Exception as e:
        result = {
            "status": 0,
            "message": e
        }
    finally:
        fileb.file.close()
    return jsonable_encoder(result)


router = APIRouter()


@router.post("/solve/q1", tags=["solve"])
async def solve_q1(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q1)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q2", tags=["solve"])
async def solve_q2(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q2)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q3", tags=["solve"])
async def solve_q3(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q3)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q4", tags=["solve"])
async def solve_q4(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q4)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q9", tags=["solve"])
async def solve_q9(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q9)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q10", tags=["solve"])
async def solve_q10(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q10)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q11", tags=["solve"])
async def solve_q10(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q11)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q12", tags=["solve"])
async def solve_q14(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q12)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q13", tags=["solve"])
async def solve_q14(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q13)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q14", tags=["solve"])
async def solve_q14(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q14)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q15", tags=["solve"])
async def solve_q15(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q15)
    return JSONResponse(content=json_compatible_results)


@router.post("/solve/q16", tags=["solve"])
async def solve_q16(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q16)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q17", tags=["solve"])
async def solve_q16(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q17)
    return JSONResponse(content=json_compatible_results)

@router.post("/solve/q23", tags=["solve"])
async def solve_q23(fileb: UploadFile = File(...)):
    json_compatible_results = process_image(fileb, routers.solve_q23)
    return JSONResponse(content=json_compatible_results)