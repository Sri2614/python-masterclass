import random

x = random.randint(2,10)
y = random.random()

myList = ['rock','paper','scissor']

z = random.choice(myList)
cards = [1,2,3,4,5,6,7,8,9,"J","S","F","A"]
random.shuffle(cards)

print(cards)