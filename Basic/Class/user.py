print('-----Practice 9-3-----')
class User:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'The user name is {self.first_name} {self.last_name}. This user is a {self.gender} and {self.age} years old.')

    def greet_user(self):
        print(f'Good day, {self.first_name} {self.last_name}!')

    def login_attempt(self):
        self.login_attempts += 1

    def reset_login(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = Privileges()

   
class Privileges:
    def __init__(self):
        self.privileges = ["Can add post","Can delete post","Can ban user","Can remove user"]

    def show_privileges(self):
        print(f"Admin's privileges includes:")
        for index, item in enumerate(self.privileges):
            print(f"{index + 1}. {item}")

user1 = User("Lee", "Jane", "Female", 18)
user2 = User("Absam", "Mousa", "Male", 24)
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

print("-----Practice 9.5-----")
user1.login_attempt()
user1.login_attempt()
print(user1.login_attempts)
user1.reset_login()
print(user1.login_attempts)

admin1 = Admin("Lee","LihKai","Male",24)
admin1.privileges.show_privileges()