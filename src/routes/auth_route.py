from fastapi import APIRouter, Body
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..schemas.auth_schema import UserCreateResponse, UserCreate, UserLogin
from ..services.auth_service import register_user, login_user

router = APIRouter(
   prefix="/auth",
   tags=["auth"]
)



   

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=UserCreateResponse)

def registration(user: UserCreate  = Body(...), db: Session = Depends(get_db)):
   return register_user(db, user)
  

@router.post('/login', status_code=status.HTTP_200_OK)
async def login(user: UserLogin = Body(...), db: Session = Depends(get_db)):
   return login_user(db, user)
   
