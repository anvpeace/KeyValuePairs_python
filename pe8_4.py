"""# 4. Create a dictionary and use loops to print keys and values: 

a) Create a dictionary, stuInfo with the keys name, gpa, and age.  Give appropriate values for each key.


 b) Use a loop and the items() method to print all keys and values. 
 
 c) Use the update() method to change the gpa to 4.0.  
 
 d) Use a loop and the keys() method to print all keys and values. 
 
 e) Add a key major with the value to the dictionary. 
 
 f) Use a loop and the values() method to print all values. 
 
 g) Use two different ways to delete gpa and age in the dictionary. 
 
 h) Print the updated dictionary. """


# a) Create a dictionary, stuInfo with the keys name, gpa, and age.  Give appropriate values for each key.

stuInfo = {
    
    "name":"Peace", "gpa": 3.9, "age": 28
    
    }

#  b) Use a loop and the items() method to print all keys and values. 

for (keys, values)  in stuInfo.items():
    print(f'{keys}: {values}')

#  c) Use the update() method to change the gpa to 4.0.  
stuInfo.update({"gpa": 4.00})

# d) Use a loop and the keys() method to print all keys and values. 

for key in stuInfo.keys():
    print(f'{key}: {stuInfo[key]}')

#  e) Add a key major with the value to the dictionary. 
stuInfo.update({"major": "IT"})


#  f) Use a loop and the values() method to print all values. 

for value in stuInfo.values():
    print(value)

#  g) Use two different ways to delete gpa and age in the dictionary. 

del stuInfo["age"]
# del stuInfo["gpa"]

# stuInfo.pop("age", None)
stuInfo.pop("gpa", None)


print(stuInfo)
