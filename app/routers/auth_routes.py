from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.controllers.auth_controllers.login_controller import handle_login
from app.controllers.auth_controllers.logout_controller import handle_logout
from app.controllers.auth_controllers.refresh_token_controller import handle_refresh_token
from app.middleware.verify_gjwt import verify_google_token
from app.models.token import Token

router = APIRouter(
    prefix="/auth",
    tags=["Auth Routes"]
)


@router.get("", response_model=Token)
async def login(google_token_verification_result: dict = Depends(verify_google_token)):
    response = handle_login(google_token_verification_result["email"])
    return response


@router.get("/refresh", response_model=Token)
async def refresh(request: Request):
    response = await handle_refresh_token(request)
    return response


@router.get("/logout")
async def logout(request: Request):
    response = await handle_logout(request)
    return response
