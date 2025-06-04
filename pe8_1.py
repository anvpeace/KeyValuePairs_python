"""
1. Determine the output displayed by the lines of code.

"""
NY = {"BX":1.42, "MN":1.63, "QS":2.25, "BN":2.56, "SI": 0.47} 

# A
"""This line of code is using square brackets `[]` to access the value associated with the key `'QS'` in the dictionary `NY`, and then it's printing that value. So, it will print the value associated with the key `'QS'` in the dictionary `NY`."""

print((NY['QS'])) 
"""This line of code is using the `get()` method to retrieve the value associated with the key `"QS"` in the dictionary `NY`, and then it's printing that value. """

print(NY.get("QS"))

# Output
"""
Both will print the value associated with the key `'QS'` in the dictionary `NY`, which is `2.25`
"""

# B

print(NY.get("LI", "Not in"))
"""This line of code uses the `get()` method to retrieve the value associated with the key `"LI"` in the dictionary `NY`, so it will print `"Not in"` since `"LI"` is not a key in the dictionary `NY`."""

print(NY.get('SI', 'absent'))
"""This line of code also uses the `get()` method to retrieve the value associated with the key `'SI'` in the dictionary `NY`. If the key `'SI'` is found in the dictionary `NY`, it will return its corresponding value. Since `'SI'` is a key in the dictionary `NY`, it will print the value associated with `'SI'`, which is `0.47`."""

print(NY.setdefault('SI', 0.48))
"""This line of code uses the `setdefault()` method to retrieve the value associated with the key `'SI'` in the dictionary `NY`. If the key `'SI'` is found in the dictionary `NY`, it will return its corresponding value. Otherwise, it will set the key `'SI'` to the specified default value `0.48` and return that value. Since `'SI'` already exists in the dictionary `NY` with a value of `0.47`, it will return the current value associated with `'SI'`, which is `0.47`. However, it won't change the value associated with `'SI'` in the dictionary."""

# Output
"""
Not in
# 0.47
# 0.47
"""

# C
print("LI" in NY)
"""
This line checks if the key `"LI"` exists in the dictionary `NY`. If `"LI"` is a key in `NY`, it will print `True`; otherwise, it will print `False`.
""" 

print('MN' not in NY)
"""
This line checks if the key `'MN'` does not exist in the dictionary `NY`. If `'MN'` is not a key in `NY`, it will print `True`; otherwise, it will print `False`.
""" 
# Output
"""
False
False
"""

# D
print(len(NY), min(NY), max(NY)) 
"""
`len(NY)`: This calculates the length of the dictionary `NY`, which is the number of key-value pairs it contains.

`min(NY)`: This returns the minimum key in the dictionary `NY` based on lexicographical order, or the smallest key alphabetically.

`max(NY)`: This returns the maximum key in the dictionary `NY` based on lexicographical order, or the largest key alphabetically.
"""

print(len(NY.items()), max(NY.keys()), min(NY.values())) 
"""
`len(NY.items())`: This calculates the length of the dictionary `NY.items()`, which returns a view object that displays a list of a dictionary's key-value tuple pairs.

`max(NY.keys())`: This returns the maximum key in the dictionary `NY` based on lexicographical order.

`min(NY.values())`: This returns the minimum value in the dictionary `NY`.
"""

# Output
"""
5 BN SI
5 SI 0.47
"""

# E
print(round(NY['QS']))
"""
This accesses the value associated with the key `'QS'` in the dictionary `NY`, then the `round` function rounds the value obtained from `NY['QS']` to the nearest integer
""" 

NY['QS'] += .3 
# This line essentially increments the value associated with the key `'QS'` in the dictionary `NY` by `0.3`

print(round(NY['QS'], 1))
# This function rounds the updated value obtained from `NY['QS']` to the nearest tenth (one decimal place).

# Output
"""
2
2.6
"""

# F
print(NY.keys())
# This prints all the keys in the dictionary `NY`.

print(list(NY.values()))
# This prints all the values in the dictionary `NY`, converting them to a list.

print(tuple(NY.items()))
# This prints all the key-value pairs (items) in the dictionary `NY`, converting them to a tuple.

# Output
"""
dict_keys(['BX', 'MN', 'QS', 'BN', 'SI'])
[1.42, 1.63, 2.25, 2.56, 0.47]
(('BX', 1.42), ('MN', 1.63), ('QS', 2.25), ('BN', 2.56), ('SI', 0.47))
"""


#G 

total = 0 
# `total = 0` initializes a variable `total` to store the sum of all values in the dictionary.

for x in NY.values(): 
# This for loop iterates over each value in the dictionary `NY`.

    total += x 
# This adds each value to the `total`.

print(f'{total:.1f}') 
# This prints the total with one decimal place.

# Output
"""
8.3
"""

# H 
total = 0 
#This initializes a variable `total` to store the sum of all values in the dictionary.
 
for x in NY:     
# This iterates over each key in the dictionary `NY`.

    total += NY[x] 
# This adds each value associated with the key `x` to the `total`.

print(f'{total:.1f}') 
# This prints the total with one decimal place.

# Output
"""
8.3
"""

# I 

for x in sorted(NY) : print(x, end = '|') 
# This iterates over the keys of the dictionary `NY` after sorting them and prints each key followed by a pipe symbol `|`.

# Output
"""
BN|BX|MN|QS|SI|
"""

# J 

"""Use a for loop to print all key names in the reversed alphabetical order (see output below). 

Example Output: SI|QS|MN|BX|BN| """
for x in sorted(NY, reverse=True):
    print(x, end='|')

# Explanation & Output
"""
sorted(NY, reverse=True): This sorts the keys of the dictionary `NY` in reverse alphabetical order.
`for x in ...` sets up a loop that iterates over each key in the sorted list.
`print(x, end='|')` prints each key followed by a pipe symbol `|`, using the `end` parameter to specify that each print statement should end with a pipe symbol rather than a newline.

Output:

SI|QS|MN|BX|BN|
"""

# K 

"""Use a for loop to print all values from max to min order (see output below).
Example Output: 2.56, 2.25, 1.63, 1.42, 0.47, """

for x in sorted(NY.values(), reverse=True):
    print(f"{x}, ", end='')

# Output
# 2.56, 2.25, 1.63, 1.42, 0.47,


# L 

if "QS" in NY: print("Queens is the most diverse county in NY.") 
# This checks if the key `"QS"` exists in the dictionary `NY`, and if it does, it prints the message.


# Output
"""
Queens is the most diverse county in NY.
"""

# M 

for x, y in NY.items():     
# This iterates over each key-value pair in the dictionary `NY`. `x` represents the key, and `y` represents the value.

    if y > 2.5: 
    # This condition checks if the value `y` associated with the current key is greater than `2.5`.

        print(f"{x} is the Kings county!") 
    # If the condition is true, it prints a message indicating that the key `x` is considered as the Kings county.

# Output
"""
BN is the Kings county!
"""

# N 

NY["SK"] = 1.49 
# This adds a new key-value pair `'SK': 1.49` to the dictionary `NY`.


print(NY) 
# This prints the updated dictionary `NY`.

# Output
"""
{'BX': 1.42, 'MN': 1.63, 'QS': 2.25, 'BN': 2.56, 'SI': 0.47, 'SK': 1.49}
"""

# O 

NY.update({"NU":1.34}) 
# This adds a new key-value pair `'NU': 1.34` to the dictionary `NY`.

print(NY) 
# This prints the updated dictionary `NY`.

# Output
"""
{'BX': 1.42, 'MN': 1.63, 'QS': 2.25, 'BN': 2.56, 'SI': 0.47, 'SK': 1.49, 'NU': 1.34}
"""
  

# P 

NY.pop("QS") 
# This removes the key-value pair with the key `"QS"` from the dictionary `NY`.

NY.popitem() 
# This removes and returns the last key-value pair from the dictionary `NY`.

print(NY)  
#  This prints the updated dictionary `NY`.

# Output
"""
{'BX': 1.42, 'MN': 1.63, 'BN': 2.56, 'SI': 0.47, 'SK': 1.49, 'NU': 1.34}
"""

# Q 

newYork = NY 
# This creates a new reference `newYork` to the same dictionary object as `NY`.

del newYork['BN'] 
# This deletes the key-value pair with the key `'BN'` from the dictionary `newYork`.

print(NY) 
# This line of code prints the dictionary `NY`.

print(newYork)
# This prints the dictionary `newYork`.  

# Output
"""
{'BX': 1.42, 'MN': 1.63, 'SI': 0.47, 'SK': 1.49, 'NU': 1.34}
{'BX': 1.42, 'MN': 1.63, 'SI': 0.47, 'SK': 1.49, 'NU': 1.34}
"""

# R 

newYork = dict(NY)
# This creates a new dictionary `newYork` with the same key-value pairs as `NY`. 

del newYork["BN"] 
# This deletes the key-value pair with the key `'BN'` from the dictionary `newYork`.v

print(len(NY))
# This prints the length of the dictionary `NY`.

print(len(newYork)) 
# This prints the length of the dictionary `newYork`.

# Output
"""
5
4
"""

# S 

NewYork = NY.copy()
"""
This creates a shallow copy of the dictionary `NY` and assigns it to `NewYork`.
""" 

NY.clear() 
# This removes all key-value pairs from the dictionary `NY`.

print(NY) 
# This prints the dictionary `NY`.

print(NewYork) 
# This prints the dictionary `NewYork`.

del NY 
# This deletes the reference to the dictionary `NY`.


print(set(NewYork)) 

# This prints the set of keys in the dictionary `NewYork`.

# Output
"""
{}
{'BX': 1.42, 'MN': 1.63, 'SI': 0.47, 'SK': 1.49, 'NU': 1.34}
{'BX', 'MN', 'NU', 'SI', 'SK'}

"""
