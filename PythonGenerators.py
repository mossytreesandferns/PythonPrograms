
nums = [1,2,3,4,5,6,7,8,9,10]

# Using list
def x_squared(num_list):
    for num in num_list:
        print(num * num)


# Using generator
def gen_x_squared(num_list):

    for num in num_list:
        yield num * num


x_squared(nums)
print(gen_x_squared(nums)) #prints type of object

gen_next_num = gen_x_squared(nums)
print(next(gen_next_num))
print(next(gen_next_num))
print(next(gen_next_num))
print(next(gen_next_num))
print(next(gen_next_num)) # going past end of list will result in "stop iteration" error

# separate for loop for printing values
for number in gen_next_num:
    print(number)

# Using list comprehension


gen_next_num = [x*x for x in nums]

for number in gen_next_num:
    print(number)

# converting back to list returns memory usage to previous levels


# Applying inbuilt python functions

total = sum(gen_next_num)
maximum = max(gen_next_num)
print(total)
print(maximum)  


# Making new functions

def power_of_two(maximum = 7):
    n = 0
    i = 0
    while i < maximum:
        yield 2 ** n
        n += 1

print(power_of_two()) 
#func_gen = [x for x in power_of_two()]
#print([square for square in func_gen])

nums = [1,2,3,4,5,6,7,8,9,10]
cubes = (x**3 for x in nums)
print([cube for cube in cubes])



