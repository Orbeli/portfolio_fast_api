from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from portfolio_rest_api.schemas import (
    Message,
    UserDB,
    UserList,
    UserResponse,
    UserSchema,
)

app = FastAPI()

database = []


@app.get(path='/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'root read'}


@app.post(
    path='/users/', status_code=HTTPStatus.CREATED, response_model=UserResponse
)
def create_user(user: UserSchema):
    created_user = UserDB(
        name=user.name,
        email=user.email,
        password=user.password,
        id=len(database) + 1,
    )

    database.append(created_user)

    return created_user


@app.get(path='/users/', status_code=HTTPStatus.OK, response_model=UserList)
def get_users():
    return {'users': database}


@app.put(
    path='/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserResponse,
)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    found_user = UserDB(
        name=user.name,
        email=user.email,
        password=user.password,
        id=user_id,
    )

    database[user_id - 1] = found_user

    return found_user


@app.delete(path='/users/{user_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    database.pop(user_id - 1)
