from dotenv import load_dotenv
from fastapi import Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from os import getenv

security = HTTPBearer()
load_dotenv()


def expired_token(exp: int):
    date = datetime.now()
    new_date = date + timedelta(hours=exp)
    return new_date


def generate_token(data: dict, expires_delta: timedelta | None = None):
    expire_minutes = getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    secret_token = getenv("SECRET_TOKEN")
    algorithm_token = getenv("ALGORITHM_TOKEN")

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=float(expire_minutes))
    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    to_encode.update({"exp": expire})
    return encode(to_encode, secret_token, algorithm=algorithm_token)


def validate_token(token, output=False):
    secret_token = getenv("SECRET_TOKEN")
    algorithm_token = getenv("ALGORITHM_TOKEN")
    try:
        if output:
            return decode(token, key=secret_token, algorithms=algorithm_token)
        decode(token, key=secret_token, algorithms=algorithm_token)
        return JSONResponse(
            content={"message": "Token valid"}, status_code=status.HTTP_200_OK)
    except exceptions.DecodeError:
        return JSONResponse(
            content={"message": "Token invalid"}, status_code=status.HTTP_401_UNAUTHORIZED)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(
            content={"message": "Token expired"}, status_code=status.HTTP_401_UNAUTHORIZED)


def auth_bearer(auth: HTTPAuthorizationCredentials = Security(security)):
    return validate_token(auth.credentials)
