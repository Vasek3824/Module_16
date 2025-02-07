from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def boot():
    return ("Главная  страница")

@app.get("/user/admin")
async def boot_1():
    return ("Вы вошли как администратор")


@app.get('/user/{user_id}')
async def user_(user_id: int):
    return (f"Вы вошли как пользователь № {user_id}")

@app.get('/user')
async def user(username: str = 'Ваня', age: int = 22):
    return (f"Информация о пользователе. Имя: {username}, Возраст: {age}")