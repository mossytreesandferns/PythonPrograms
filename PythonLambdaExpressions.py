

def parab(x):
    return x**2 + 5
print(parab(3))

# lamda input: expression
result = lambda x: x**2 + 5
print(result(3))

zresult = lambda x,y: x**2 + y**2
print(zresult(3,3))

first_name = 'Isabelle'
last_name = 'Magician'
full_name = lambda f,l: f.upper() + ' ' + l.lower()
print(full_name(first_name,last_name))

def quadratic(a,b,c):
    return lambda x: a*x**2 + b*x + c

example = quadratic(5,2,5)
print(example(2),example(0)) 

print(quadratic(3,2,9)(0), quadratic(3,2,9)(1))

