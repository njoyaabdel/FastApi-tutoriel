from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from main.controllers.routers import Post,user,auth,vote
from main.models import post
from main.schemas import postschemas
from sqlalchemy.orm import Session
from main.core.dependencies import engine


# post.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}



# @app.post("/", status_code=status.HTTP_201_CREATED, response_model=postschemas.Post)
# def create_posts(post: postschemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
#     #                (post.title, post.content, post.published))
#     # new_post = cursor.fetchone()

#     # conn.commit()

#     new_post = post.Post(owner_id=current_user.id, **post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)

#     return new_post