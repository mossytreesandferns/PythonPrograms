try:
    print(x)
except:
    print("An exception has occurred. You have not defined 'x'")    


try:
    print(x)
except NameError:
    print("You have not defined 'x'") 
except:
    print("Another exception has occurred")    

# No Errors
try:
    print('farfegnugen')  
except:
    print('An exception has occurred.')
else:
    print('No error occurred.') 

# Finally executes whether there is an error or not
try:
    print('farfegnugen')  
except:
    print('An exception has occurred.')
else:
    print('No error occurred.')
finally:
    print('Happy Trails until we meet again.')   

# Writing to files
try:
    f = open('practice.txt','w')   
    f.write('This is a practice string of text.')
except:
    print('Something went wrong writing to the text file.')
else:
    print('Writing file complete.')
finally:
    f.close()   

# Value Errors
try:
    print(int('dog'))
except ValueError:
    print("A string is not an integer") 
else:
    print('pass')
finally:
    print("Hello World")    

