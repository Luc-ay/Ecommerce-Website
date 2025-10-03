from passlib.context import CryptContext
from typing import Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from ..config.secret import secret
from ..schemas.auth_schema import USERROLE

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_auth_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=secret.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret.SECRET_KEY, algorithm=secret.ALGORITHM)
    return encoded_jwt


def verify_auth_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, secret.SECRET_KEY, algorithms=[secret.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    

async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    return verify_auth_token(token)


async def get_admin_user(current_user: dict = Depends(get_current_user)) -> dict:
    if USERROLE(current_user.get("role")) != USERROLE.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin Access Required")
    return current_user

async def get_vendor_user(current_user: dict = Depends(get_current_user)) -> dict:
    if USERROLE(current_user.get("role")) != USERROLE.VENDOR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Vendor Access Required")
    return current_user