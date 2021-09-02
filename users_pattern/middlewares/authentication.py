import os

from fastapi_users.authentication import CookieAuthentication
from dotenv import load_dotenv

load_dotenv()
SECRET = os.getenv("SECRET")

auth_backends = []

cookie_authentication = CookieAuthentication(secret=SECRET, lifetime_seconds=3600, cookie_secure=False)

auth_backends.append(cookie_authentication)