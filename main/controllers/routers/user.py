from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from main.core.dependencies import get_db
from main.models import post
from main.schemas import postschemas
from main.utils import auth_utils

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

# /users/
# /users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=postschemas.UserOut)
def create_user(user: postschemas.UserCreate, db: Session = Depends(get_db)):

    # hash the password - user.password
    hashed_password = auth_utils.hash(user.password)
    user.password = hashed_password

    new_user = post.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/{id}', response_model=postschemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db), ):
    user = db.query(post.User).filter(post.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user