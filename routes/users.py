from fastapi import APIRouter, HTTPException, status
from models.users import UserSingIn, User


user_routs = APIRouter(
    tags=["User"]
)


users = {}


@user_routs.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with supplied username exists"
        )
    users[data.email] = data
    return {
        "message": "User successfully registered"
    }


@user_routs.post("/signin")
async def sign_user_in(user: UserSingIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User doesn't exist"
        )
    if user.password != users[user.email].password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential passed"
        )

    return {
        "message": "User signed in successfully"
    }
