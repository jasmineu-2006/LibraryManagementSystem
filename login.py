def login():
    print("Login module updated by teammate")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "admin123":
        print("Login successful")
        return True
    else:
        print("Invalid credentials")
        return False
