def palindrome(string):
    lst = []
    for letter in string:
        lst.append(letter)
    rev = lst[::-1]
    if lst == rev: 
        return True
    else: return False    

print(palindrome('anta'))    





lst=[1,2,3,4,5]
print(lst)
lst.reverse() #reverse in place, don't assign to variable
print(lst)

lst = [1,2,3,4,5]
rev = lst[::-1]
print(rev)
