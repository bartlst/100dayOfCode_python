class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        print("NEW USER BEING CREATED...")


user_1 = User("001", "admin")

print(user_1.username)
