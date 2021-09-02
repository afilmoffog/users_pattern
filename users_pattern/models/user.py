from fastapi_users import models


class User(models.BaseUser):
    username: str
    password: str
    full_name: str = None
    is_creator: bool = None
    payment_requisites: str = None
    bio: str = None
    profile_pic: list = None


class UserCreate(models.BaseUserCreate):
    username: str


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    is_verified = True
