
# Pick a number between 0 and 3999
def roman_numeral(number):
    num = str(number)
    lst = []
    rom_lst = []
    thous = {'1':'M','2':'MM','3':'MMM'}
    hund = {'1':'C','2':'CC','3':'CCC','4':'CD','5':'D','6':'DC','7':'DCC','8':'DCCC','9':'CM'}
    tens = {'1':'X','2':'XX','3':'XXX','4':'XL','5':'L','6':'LX','7':'LXX','8':'LXXX','9':'XC'}
    ones = {'1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX'}
    for digit in num:
        lst.append(digit)
    if len(lst) == 4:
        rom_lst.append(thous[lst[0]])
        rom_lst.append(hund[lst[1]])
        rom_lst.append(tens[lst[2]])
        rom_lst.append(ones[lst[3]])     
    elif len(lst) == 3:
        rom_lst.append(hund[lst[1]])
        rom_lst.append(tens[lst[2]])
        rom_lst.append(ones[lst[3]])      
    elif len(lst) == 2:
        rom_lst.append(tens[lst[2]])
        rom_lst.append(ones[lst[3]])       
    else: 
        rom_lst.append(ones[lst[0]]) 

    return ''.join(rom_lst)                

print(roman_numeral(3594))                   

    

    
    
    



# num = 2000
# snum = str(num)
# print(snum[0])    