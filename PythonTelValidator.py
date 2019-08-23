"""Write a program that validates a US phone number"""
import re

def valid_phone(phone):
    #phone = str(num)
    len_list = [10,12,13,14]

    if len(phone) not in len_list:
        return "I'm sorry, that is not a valid US phone number"

    if len(phone) == 10:
        if not phone.isdigit():
            return "I'm sorry, that is not a valid US phone number"
        else:    
            return "That is a valid US phone number"

    elif len(phone) == 12:
        regex = '\d{3}.\d{3}.\d{4}'
        if re.search(regex,phone): 
            return "That is a valid US phone number"
        else:    
            return "I'm sorry, that is not a valid US phone number"
    elif len(phone) == 13:
        regex = '\(\d{3}\)\d{3}.\d{4}'
        if re.search(regex,phone):
            return "That is a valid US phone number"
        else: return "I'm sorry, that is not a valid US phone number"
    else:
        regex = '\(\d{3}\).\d{3}.\d{4}'  
        rex = '\d.\d{3}.\d{3}.\d{4}'  
        if re.search(regex,phone) or re.search(rex,phone):
            return    "That is a valid US phone number"
        else: 
            return "I'm sorry, that is not a valid US phone number"
            

print(valid_phone('555 555 5555'))           






