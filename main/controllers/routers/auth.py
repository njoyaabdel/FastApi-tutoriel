from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from main.core import dependencies
from main.models import post
from main.schemas import postschemas
from main.utils import auth_utils

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=postschemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(dependencies.get_db)):

    user = db.query(post.User).filter(
        post.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not auth_utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    # create a token
    # return token

    access_token = auth_utils.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}