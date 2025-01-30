from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
import jwt
from dotenv import load_dotenv
import os

from app.config.database import user_collection
from app.controllers.auth_controllers.tokens_controller import create_access_token

load_dotenv()

ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
REFRESH_TOKEN_SECRET = os.getenv("REFRESH_TOKEN_SECRET")
ALGORITHM = os.getenv("ALGORITHM")


async def handle_refresh_token(request: Request):
    try:
        refresh_token = request.cookies.get('jwt')
        print(refresh_token)
        print(request.headers)
    except Exception as e:
        print(f'Exited with Exception: {e}. Setting refresh token to None')
        refresh_token = None

    if refresh_token is not None:
        found_user = user_collection.find_one({"refresh_token": refresh_token})
        print(found_user)

        if not found_user:
            raise HTTPException(403, detail="Forbidden!")

        try:
            decoded_refresh_token = jwt.decode(
                refresh_token,
                REFRESH_TOKEN_SECRET,
                algorithms=ALGORITHM,
                verify=True)
            print(decoded_refresh_token)
        except Exception as e:
            print(f'Exited with Exception: {e}')
            raise HTTPException(403, detail="Forbidden!")

        if decoded_refresh_token["user_email"] == found_user["user_email"]:
            access_token = create_access_token(
                found_user["user_email"],
                found_user["user_name"])
            data_to_return = {
                "access_token": access_token,
                "token_type": "Bearer",
                "user_email": found_user["user_email"]
            }
            response = JSONResponse(content=data_to_return)
            return response
        else:
            raise HTTPException(403, detail="Forbidden")

    else:
        raise HTTPException(401, detail="Could not authorize User!")
