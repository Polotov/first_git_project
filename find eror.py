bd_username = "testuser"
bd_password = "testpassword"

def auth(tries: int):
    count = 0
    while count < tries:
        username = input("введите имя поль")
        password = input("введите пароль")
        if username == bd_username and password == bd_password:
            print("Добро пожаловать")
            break
        else:
            print("ввели неверные данные! попробуйте еще раз!")
            count += 1
auth(3)