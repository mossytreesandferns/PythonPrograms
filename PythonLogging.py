import logging

"""levels: 
debug 10, general information
info 20, confirmation that things are working as expected
warning 30, something unexpected happened, there might be problems, default level of logging()
error 40, serious problem, program couldn't perform a function
critical 50, serious error, the program may not be able to keep running
"""

logging.basicConfig(filename='logfile.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')# setting level, creating logfile,setting format

def squared(x):
    return x * x

def add(a,b):
    return a + b  

def fib(n):
    if n <=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2) + fib(n-1)    


square_result = squared(9)
logging.info(square_result)
logging.debug(square_result) # default is set to warning
logging.warning(square_result)
logging.error(square_result)
logging.critical(square_result)

add_result = add(3,7)
logging.info(add_result)
logging.debug(add_result) # default is set to warning
logging.warning(add_result)
logging.error(add_result)
logging.critical(add_result)

fib_result = fib(6)
print(fib_result)


import random
class Dice:
    def dice(self):
        face1 = random.randint(1,7)
        face2 = random.randint(1,7)
        logging.info('You rolled: ' + str((face1, face2)))

    def double_score(self):
        face1 = random.randint(1,7)
        face2 = random.randint(1,7)
        logging.info('You rolled a double score: ' + str((face1*2, face2*2)))

current_roll = Dice()
current_roll.double_score()
current_roll.dice()