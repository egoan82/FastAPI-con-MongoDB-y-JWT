from fastapi import Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from os import getenv

security = HTTPBearer()


def expired_token(exp: int):
    date = datetime.now()
    new_date = date + timedelta(hours=exp)
    print(date)
    print(new_date)
    return new_date


def generate_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=float(getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))

    print(datetime.utcnow())
    print(expire)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, getenv(
        "SECRET_TOKEN"), algorithm=getenv("ALGORITHM_TOKEN"))
    return encoded_jwt


def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("SECRET_TOKEN"), algorithms=getenv("ALGORITHM_TOKEN"))
        decode(token, key=getenv("SECRET_TOKEN"),
               algorithms=getenv("ALGORITHM_TOKEN"))
    except exceptions.DecodeError:
        return JSONResponse(
            content={"message": "Token invalid"}, status_code=status.HTTP_401_UNAUTHORIZED)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(
            content={"message": "Token expired"}, status_code=status.HTTP_401_UNAUTHORIZED)


def auth_bearer(auth: HTTPAuthorizationCredentials = Security(security)):
    return validate_token(auth.credentials)
