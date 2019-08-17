
from math import pi

def area(r):
    area = pi*r**2
    return area

print(area(1))  

""" map() applies a function to an iterable"""

radii = [2,4,6,8,10]

for r in radii:
    print(area(r))

print(list(map(area, radii))) 

elevations_ft = [('Seatte',520),('San Francisco',52),('Los Angeles',285),('Anchorage',102)]
# 1m = 3.28ft
ft_to_meters = lambda data: (data[0], data[1]/(3.28))
print(list(map(ft_to_meters, elevations_ft)))


"""filter() allows iterables to be filtered out"""

# numbers
import statistics
nums = [1,2,3,4,5,7,6,7,8,9]
mean = statistics.mean(nums)
mode = statistics.mode(nums)
print(mean, mode)
print(list(filter(lambda x: x > mean, nums)))
print(list(filter(lambda x: x < mode, nums)))


strings = ['word','', '', 'syntax','adjective','fine']
print(list(filter(None, strings)))


