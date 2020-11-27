def register_to_bd(username,password,check_password):
    if password == check_password:
        file1 = open("database.txt","w")
        result = username + "\n" + password
        file1.write(result)

register_to_bd("asdasd","123","123")