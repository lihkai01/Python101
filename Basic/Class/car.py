class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
# Child Class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialise attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car dosen't need a gas tank!")


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

# Class Instances
my_car = Car('audi', 'a4', 2021)
print(my_car.get_descriptive_name())

my_car.odometer_reading = 45
my_car.read_odometer()

my_car.update_odometer(39)
my_car.read_odometer()

my_car.update_odometer(54)
my_car.read_odometer()

used_car = Car("Produa","Ativa",2024)
print(used_car.get_descriptive_name())

used_car.update_odometer(30456)
used_car.read_odometer()

used_car.increment_odometer(1000)
used_car.read_odometer()

my_tesla = ElectricCar('tesla','model y',2023)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("-----Practice 9.9-----")
my_byd = ElectricCar('BYD','atto 3',2022)
my_byd.battery.get_range()
my_byd.battery.upgrade_battery()
my_byd.battery.get_range()