
# Dictionary Comprehension

centimeters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(centimeters.keys())
print(centimeters.values())
print(centimeters.items())

inches_in_centimeters = {k:v*2.5 for (k,v) in centimeters.items()}
print(inches_in_centimeters)

tool_length = {k:v for (k,v) in inches_in_centimeters.items() if v>2.5}
print(tool_length)

special_tools = {k:v for (k,v) in inches_in_centimeters.items() if v>2 and v%2 ==0}
print(special_tools)

tool_words = {k:("whole" if v%1==0 else"fraction") for (k,v) in inches_in_centimeters.items()}
print(tool_words)


# List comprehension
nums = [1,2,3,4,5,6,7,8,9,10] 
squares = [i*i for i in nums]
squares_of_evens = [i*i for i in nums if i%2==0]
print(squares)
print(squares_of_evens)

nums = [i for i in range(1,11)] 
squares = [i*i for i in nums]
squares_of_evens = [i*i for i in nums if i%2==0]
print(squares)
print(squares_of_evens)

words = ['yellow', 'and', 'black', 'bumblebee']
letters = [words[3] for word in words]
print(letters)

nums_letts = 'words, 1234, letters'
nums = [n for n in nums_letts if n.isdigit()]
print(nums)

nums = [n for n in 'words, 1234, letters' if n.isdigit()]
print(nums)