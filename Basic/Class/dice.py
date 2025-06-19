import random

class Die:
    def __init__(self,sides):
        self.sides = sides

    def roll_die(self):
        return random.randrange(1,self.sides)

die = Die(20)
for i in range(10):
    print(f"Roll {i+1}: {die.roll_die()}")