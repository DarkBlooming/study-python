class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def update_name(self, new_name):
        self.name = new_name
        print(f"User's name updated to: {self.name}")

    def update_email(self, new_email):
        self.email = new_email
        print(f"User's email updated to: {self.email}")

    def delete_user(self):
        print(f"User with ID {self.user_id} is deleted.")
        self.name = None
        self.email = None

if __name__ == "__main__":
    user = User(user_id = 1, name = "Hannah Smith", email = "hannahco@gmail.com")
    print(f"User: ID = {user.user_id}, Name = {user.name}, Email = {user.email}")

    user.update_name("Hannah Lewis")
    user.update_email("hannahxo@gmail.com")

    user.delete_user()
