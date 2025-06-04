"""dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} 
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50} 

Example Output: {‘Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50} 
"""

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} 
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50} 


dict1.update(dict2)
# The `update()` method adds all the key-value pairs from `dict2` into `dict1`. 

print(dict1)



