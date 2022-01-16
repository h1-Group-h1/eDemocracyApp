from typing import List
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from deta import Deta
from schemas import *
app = FastAPI()
deta = Deta("a0svha7u_zdyC9BJGJLCzv36DdG5Y2RtHPMKiwK2Y")

users = deta.Base("users")
polls = deta.Base("polls")
organisations = deta.Base("organisations")


origins = ['https://localhost:3000']



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def validate(response):
    if response:
        return response
    raise HTTPException(400, 'something went wrong.')

@app.get("/")
def read_root():
    return {'Ping': 'Pong'}
"""

@app.get("/api/post")
async def get_post():
    response = await fetch_all()
    return response

@app.get("/api/post{title}", response_model=Post)
async def get_post_by_id(title):
    response = await fetch_post(title)
    if response:
        return response
    raise HTTPException(404, f'there is no POST item with this (id)')


@app.post("/api/post", response_model=Post)
async def new_post(post: Post):
    response = await create_post(post.dict())
    if response:
        return response
    raise HTTPException(400, 'bad request')

    

@app.put("/api/post{title}", response_model=Post)
async def put_post(title:str, description:str):
    response = await update_post(title, description)
    if response:
        return response
    raise HTTPException(404, f'there is no Post item with this (id)')

@app.delete("/api/post{title}")
async def delete_post(title):
    response = await delete_post(title)
    if response:
        return 'success'
    raise HTTPException(404, f'there is no Post item with this (id) to delete')

"""
# User management
@app.get("/users/{key}", response_model=User)
def get_user_by_key(key: str):
    user = users.get(key)
    return validate(user)

@app.get("/users/", response_model=List[User])
def get_all_users():
    response = users.fetch()
    return validate(response.items)

@app.post("/users/add", response_model=User )
def new_user(user: UserCreate):
    user = users.put(user.dict())
    print(user)
    return user

@app.delete("/users/delete/{key}")
def app_delete_user(key: str):
    users.delete(key)

# Poll management

@app.post("/polls/add", response_model=Poll)
def new_poll(poll: PollCreate):
    poll = polls.put(poll.dict())
    print("Ok")
    return validate(poll)

@app.post("/poll/{key}", response_model=Poll)
def get_poll_by_id(key: str):
    poll = polls.get(key)
    return validate(poll)

@app.post("/polls/get/all", response_model=List[Poll])
def get_all_polls():
    response = polls.fetch()
    return validate(response.items)

@app.delete("/polls/delete/{key}")
def delete_poll(key: str):
    polls.delete(key)

@app.post("/polls/add_vote/{key}/{choice_id}", response_model=Poll)
def add_vote(key: str, choice_id: int):
    # check if user is in organisation. For later when we do oauth
    poll = get_poll_by_id(key)
    found = False
    for choice in poll["choices"]:
        if choice["id"] == choice_id:
            found = True
            break
    if not found:
        raise HTTPException(404, "Unable to add choice") # be ambiguous to avoid hackers
    for result in poll["results"]:
        if result["choice"] == choice_id:
            result["votes"] += 1
            break
    updates = {"results": poll["results"]}
    print(poll)
    poll = polls.update(updates, key)
    
    return validate(polls.get(key))

"""
@app.post("/org/add/{user_id}", response_model=Organisation)
def add_org(user_id: int):
    pass

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.delete("/users/delete/{id}/")
async def delete_user(id):
    return True


@app.put("/users/email/{new_email}/")
async def update_user_email(id, new_email):
    return True

@app.put("/users/name/{new_name}/")
async def update_user_name(id, new_name):
    return True

@app.put("/users/name/{new_password}/")
async def update_user_password(id, new_password):
    return True
"""
