from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.config.database import user_collection


async def handle_logout(request: Request):
    try:
        refresh_token = request.cookies.get("jwt")
    except Exception as e:
        print(f"Exited with Exception {e}")
        refresh_token = None

    try:
        if refresh_token is not None:
            clear_refresh_token = {"$set": {"refresh_token": ""}}
            user_collection.update_one({"refresh_token": refresh_token}, clear_refresh_token)
            response = JSONResponse(content={"message": "Logout success!"}, status_code=401)
            response.delete_cookie(
                key="jwt",
                httponly=True,
                samesite='none',
                secure=True
            )
            return response
        else:
            return JSONResponse(
                content={
                    "message": "Logout success!"
                },
                status_code=401
            )
    except Exception as e:
        print(f"Exited with Exception {e}")
        raise HTTPException(status_code=400, detail="Bad Request")