# Class Practice
print("-----Practice 9-1/9-2-----")
class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This is a {self.type} restaurant called {self.name}.")

    def open_restaurant(self):
        print(f"{self.name} is open!")

    def set_number_served(self, serve):
        self.number_served = serve
        print(f"{self.name} served {self.number_served} dishes overall.")

    def increment_number_served(self, additional_serve):
        self.number_served += additional_serve
        print(f"{self.name} served {additional_serve} dishes today, and total {self.number_served} dishes overall.")

class IceCreamStand(Restaurant):
    def __init__(self, name, type="Ice Cream Stall"):
        super().__init__(name, type)
        self.flavors = ['Vanila','Chocolate','Strawberry']

    def display_flavour(self):
        print(f"{self.name} serve {self.flavors} ice creme.")

my_restaurant = Restaurant("Happy Eat", "Korean")
print(my_restaurant.name)
print(my_restaurant.type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


print("-----")
my_rest1 = Restaurant("Hua Yang", "Chinese")
my_rest2 = Restaurant("Pak Sembor", "Malay")
my_rest3 = Restaurant("Zus Coffee", "English")
my_rest1.describe_restaurant()
my_rest2.describe_restaurant()
my_rest3.describe_restaurant()

print("-----Execerse 9.4-----")
my_restaurant.set_number_served(30)
my_restaurant.increment_number_served(50)

print("-----Execerse 9.6-----")
my_ice = IceCreamStand('IceBlog')
my_ice.display_flavour()

