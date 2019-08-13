
# immutable dtypes, not lists, sets, dicts


"""Python hash() Method"""

import hashlib

print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)

var = hash('string')
var2 = hash(45)
var3 = hash(3.14)
print(var, var2, var3)

string = hashlib.md5(b"This is a string that can be hashed") # b tells the computer that the string should be converted to bytes
hexs = string.hexdigest()
#inp = input("What string would you like to hash? ")
#inps = hashlib.md5(inp.encode())

string2 = hashlib.sha384(b"This is another string that can be hashed")
hex2 = string2.hexdigest()

print(hexs, hex2) #inps,


"""Hash Functions Using Lists"""

#List of tuples to dictionary

list_of_tshirts = [(1,'frog'),(2,'flower'),(3,'band'),(4,'statepark'),(5,'country')]
def new_tuple(list_of_tuples, key, value):
    list_of_tuples.append((key,value)) #appends duplicate key values

def search_tup_dict(list_of_tuples, key):
    for item in list_of_tuples:
        if item[0] == key:
            return item[1]  

new_tuple(list_of_tshirts, 6, 'hotel')
print(list_of_tshirts)      
search_tup_dict(list_of_tshirts, 2) 


#Simple hash function

first_hash = [None] * 15
print(first_hash)

def basic_hashing(key):
    return key % len(first_hash)

print(basic_hashing(15))    
print(basic_hashing(10))  
print(basic_hashing(18))  

def insert(hash_table, key, value): # Does not account for collisions, previous data is overwritten
    hash_key = basic_hashing(key)
    hash_table[hash_key] = value 
insert(first_hash, 12, "frog") 
insert(first_hash, 15, "satchel" )
print(first_hash)
insert(first_hash, 15, "backbpack")
print(first_hash)

#Use list of lists to prevent overwriting of data
third_hash = [[] for x in range(15)]
print(third_hash)


def better_hashing(hash_table, key):
    return key % len(hash_table)

print(better_hashing(third_hash, 18))   

def insert(hash_table, key, value):
    hash_key = better_hashing(hash_table, key)
    hash_table[hash_key].append(value)

insert(third_hash, 18, "elephant")
insert(third_hash,18, "giraffe")
print(third_hash)  


# Creating a hash table of a list of lists of tuples
third_hash = [[] for x in range(15)]
def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for kv in enumerate(bucket): 
        k,v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value)) 
    else:
        bucket.append((key, value)) 

# Practice enumerate
x = enumerate(['ball','coin','cat'])
print(list(x))           

# Call latest hash function
insert(third_hash, 18, "chihuahua")
insert(third_hash, 18, "poodle")
insert(third_hash, 15, "doberman")
print(third_hash)


# Search hash table
def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v

print(search(third_hash, 0))

# Deleting values 
def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for kv in enumerate(bucket):
        k, v = kv
        if key == k:
            del hash_table[hash_key] 
    print(hash_table)             
   
#print(third_hash[0])
#print(third_hash[0][0])
#print(third_hash[0][0][0])

delete(third_hash,7)
delete(third_hash,0)
