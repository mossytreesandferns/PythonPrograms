# Recursive
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(5)) 


def fibo(n):
    if n < 0:
        pass
    elif n <= 1:
        return 0    
    else:
        return fib(n-2) + fib(n-1)

print(fibo(5)) 

def fibon(n):
    if n ==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibon(n-1) + fibon(n-2)    
print(fibon(5))

for i in range(11):
    print(i, fibon(i))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))        


def xy_add(x, y):
    if x == 0:
        return y
    else:
        return xy_add(x-1, x + y)

print(xy_add(7,6))    

def reversing(string):
    if len(string) ==0:
        return string
    else:
        return reversing(string[1:]) + string[0]

print(reversing('palindrome'))


#Memoization

fib_store = {}
def fibon(n):
    # use dictionary to store values, save runtime from repeats
    if n in fib_store:
        return fib_store[n]

    # original function with variation
    if n ==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        to_store = fibon(n-1) + fibon(n-2)
        # store new values in dictionary
        fib_store[n] = to_store
        return to_store 

    

for i in range(1,1001):
    print(i, fibon(i))    
