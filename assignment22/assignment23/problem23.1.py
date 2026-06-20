class InvalidUsernameError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class ShortUsernameError(Exception):
    pass


class LoginSystem:
    def __init__(self, users):
        self.users = [user.lower() for user in users]

    def login(self, username):
        if len(username) < 4:
            raise ShortUsernameError("ShortUsernameError")

        if not username.isalpha():
            raise InvalidUsernameError("InvalidUsernameError")

        if username.lower() not in self.users:
            raise UserNotFoundError("UserNotFoundError")

        print("Login Successful")


# Input
n = int(input())
users = []

for _ in range(n):
    users.append(input())

username = input()

# Processing
system = LoginSystem(users)

try:
    system.login(username)
except Exception as e:
    print(e)