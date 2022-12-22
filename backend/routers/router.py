from fastapi import File, UploadFile, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

from .q1_10.q1 import solve


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
    json_compatible_results = process_image(fileb, solve)
    return JSONResponse(content=json_compatible_results)
