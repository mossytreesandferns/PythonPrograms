import random

# .random()
for x in range(5):
    print(random.random()) #.random() returns float betw 0 and 1

# .randint()
for x in range(5):
    print(random.randint(10,30))   

# Choosing from random list     
pets = ['turtle','frog','mantis','cat','bees']
first_feed = random.choice(pets)
print(first_feed)


# Create random die-roller object
import random
class Dice:
    def dice(self):
        face1 = random.randint(1,7)
        face2 = random.randint(1,7)
        return face1, face2


current_roll = Dice()
print("You rolled " + str(current_roll.dice()))
