
cost_items = [1.23,5.47,4.44,3.99,5.46,4.88,12.00]

def cash_reg(lst):
    total = 0
    for i in lst: # Note difference between i in lst and i in range(len(lst))
        total += i
    return total

print(cash_reg(cost_items))
print(cost_items[0] + cost_items[1])   
