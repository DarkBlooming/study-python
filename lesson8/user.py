class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

user = User("Sarah", "cool_sar@gmail.com", "secure_password123")

print("Name:", user.get_name())
print("Email:", user.get_email())
print("Password:", user.get_password())

user.set_name("Hannah")
user.set_email("hannahxo@gmail.com")
user.set_password("new_secure_password456")

print("\n>--After update--<")
print("Name:", user.get_name())
print("Email:", user.get_email())
print("Password:", user.get_password())
