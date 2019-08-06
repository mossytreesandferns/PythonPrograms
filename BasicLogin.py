
#!/usr/bin/env python
import sys

names = ['Theresa', 'Isabelle', 'Mariah', 'Yvette', 'Diana']
passwords = ['password','leaf','horizon','Schmetty','MichaelJackson']

name = input('Please enter your name: ')

if name not in names:
    print("I'm sorry, you are not on the electronic guest list")
    name = input('Please enter your name: ')
    if name not in names:
        print("I'm sorry, you are not on the electronic guest list")
        sys.exit()

password = input('Please enter your password: ')

if (password not in passwords) or (names.index(name) != passwords.index(password)):
    print("I'm sorry that password is incorrect. Please try again.") 
    password = input('Please enter your password: ')

if (password not in passwords) or (names.index(name) != passwords.index(password)):
    print("I'm sorry, you have used up your password attempts.")
    sys.exit()

password2 = input("Please enter your password again for verification: ")


if password != password2:
    print("I'm sorry, you have used up your password attempts.")
    sys.exit()
else:
    print('Congratulations, you were accepted into an imaginary club of special people. Yay.')   
