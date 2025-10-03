from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.user_model import User
from ..schemas.auth_schema import UserCreate, UserLogin
from ..config.security import hash_password, verify_password, create_auth_token


def register_user(db: Session, user: UserCreate):
    
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    db_username = db.query(User).filter(User.username == user.username).first()
    if db_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    
    
    hashed_password = hash_password(user.password)
    
    
    new_user = User(email=user.email, username=user.username, password=hashed_password, role= "USER")
    
    # Save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user 

def register_vendor(db: Session, user: UserCreate):
    
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    db_username = db.query(User).filter(User.username == user.username).first()
    if db_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    
    
    hashed_password = hash_password(user.password)
    
    
    new_user = User(email=user.email, username=user.username, password=hashed_password, role="VENDOR")
    
    # Save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user 

def register_admin(db: Session, user: UserCreate):
    
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    db_username = db.query(User).filter(User.username == user.username).first()
    if db_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    
    
    hashed_password = hash_password(user.password)
    
    
    new_user = User(email=user.email, username=user.username, password=hashed_password, role="ADMIN")
    
    # Save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user 


def login_user(db: Session, user: UserLogin):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    if not verify_password(user.password, str(db_user.password)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    get_token = create_auth_token(data={"sub": str( db_user.id), "role": db_user.role.value})
    
    return {"access_token": get_token, "token_type": "bearer"}
    