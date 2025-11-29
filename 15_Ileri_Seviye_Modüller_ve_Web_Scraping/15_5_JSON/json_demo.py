import json
import os


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.is_logged_in = False
        self.current_user = None

        # Load users from .json file.
        self.load_users()

    def load_users(self):
        try:
            if os.path.exists("users.json"):
                with open("users.json", "r", encoding="utf-8") as file:
                    users = json.load(file)
                    for user in users:
                        user = json.loads(user)
                        newUser = User(
                            username=user["username"],
                            password=user["password"],
                            email=user["email"],
                        )
                        self.users.append(newUser)
                print(self.users)
        except Exception as er:
            print(f"Load error, file might be empty.-> {er}")

    def register(self, user: User):  #  Registering
        self.users.append(user)
        self.save_to_file()  #  Saving for the new user
        print("User has been created.")

    def login(self, username, password):
            for user in self.users:
                if user.username == username and user.password == password:
                    self.is_logged_in = True
                    self.current_user = user
                    print("Logged in.")
                    break
            if not self.is_logged_in:
                print("Wrong credentials.")

    def logout(self):
        print(f"User {self.current_user.username} logged out.")
        self.is_logged_in = False
        self.current_user = None

    def identity(self):
        if self.is_logged_in:
            print(f"User {self.current_user.username} is in.")
        else:
            print("You didn't logged in.")

    def save_to_file(self):
        dict_list = []

        for user in self.users:
            dict_list.append(json.dumps(user.__dict__))

        with open("users.json", "w", encoding="utf-8") as file:
            json.dump(dict_list, file)


repository = UserRepository()

while True:
    print("Menu".center(59, "*"))
    choice = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nChoice: ")

    match choice:
        case "1":  # Register
            username = input("Username: ")
            password = input("Password: ")
            email = input("email: ")

            user = User(username=username, password=password, email=email)
            repository.register(user)

        case "2":  # Login
            if repository.is_logged_in:
                print("You already logged in. If you want to log in to another user, please logout first.")
            else:
                username = input("Username: ")
                password = input("Password: ")
                repository.login(username=username, password=password)

        case "3":  # Logout
            if repository.is_logged_in:
                repository.logout()
            else:
                print("You didn't logged in.")

        case "4":  # Displey Username
            repository.identity()

        case "5":  # Exit
            print("Exiting program...")
            print("-" * 59)
            break

        case _:  # Default
            print("-" * 59)
            print("Invalid choice, please select a valid option from the menu.")
