from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate, UserLogin, Token
from auth_utils import get_password_hash, verify_password, create_access_token
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/register", response_model=Token)
async def register(request: Request, user: UserCreate, db: Session = Depends(get_db)):
    # Log the raw request
    body = await request.body()
    logger.info(f"Raw request body: {body}")
    logger.info(f"Parsed user data: {user}")
    
    try:
        # Check if user exists
        db_user = db.query(User).filter(User.email == user.email).first()
        if db_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )
        
        # Create new user
        hashed_password = get_password_hash(user.password)
        db_user = User(
            email=user.email,
            name=user.name,
            hashed_password=hashed_password,
            role="customer"
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        # Create token
        access_token = create_access_token(
            data={"sub": db_user.email},
            expires_delta=timedelta(minutes=30)
        )
        
        return {"access_token": access_token, "token_type": "bearer"}
    
    except Exception as e:
        logger.error(f"Registration error: {str(e)}")
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Registration failed: {str(e)}"
        )