from fastapi import HTTPException
from starlette.responses import JSONResponse

from app.config.database import user_collection
from app.controllers.auth_controllers.tokens_controller import create_access_token, create_refresh_token


def handle_login(user_email: str):
    try:
        user_email = user_email

        found_user = user_collection.find_one(
            {"user_email": user_email}
        )

        refresh_token = None
        access_token = None

        if found_user:
            refresh_token = create_refresh_token(found_user["user_email"], found_user["user_name"])
            access_token = create_access_token(found_user["user_email"], found_user["user_name"])

        if refresh_token is not None and access_token is not None:
            update_data = {"$set": {"refresh_token": refresh_token}}
            user_collection.update_one({"user_email": found_user["user_email"]}, update_data)
            data_to_return = {
                "access_token": access_token,
                "token_type": "Bearer",
                "user_email": found_user["user_email"]
            }
            response = JSONResponse(content=data_to_return)
            response.set_cookie(
                key="jwt",
                value=refresh_token,
                expires=3600,
                httponly=True,
                samesite='none',
                secure=True
            )
            return response
        else:
            raise HTTPException(status_code=401, detail="Could not authenticate User!")
    except Exception as e:
        print(f"Exited with Exception {e}")
        raise HTTPException(status_code=401, detail="Could not authenticate User!")
