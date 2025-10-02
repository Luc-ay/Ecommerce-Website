from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
# from models import user_model, items_model
from .config import database
from .routes.auth_route import router as auth_route


app = FastAPI()


database.Base.metadata.create_all(bind=database.engine)

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "details": str(exc),  # optional: include this for debugging
            # "trace": traceback.format_exc()  # optional: for full trace (not in production)
        },
    )

app.include_router(auth_route)