import random

class Lottery:
    def __init__(self):
        self.base = ('a','k','e','t','l',1,2,3,4,5,6,7,8,9,0)

    def open_ticket(self):
        self.ticket = random.sample(self.base,4)
        print(self.ticket)
        print('Any ticket match the above win')

my_lottery = Lottery()
my_lottery.open_ticket()
