"""
2. Convert the following two lists into one dictionary:  
keys = ['Ten', 'Twenty', ‘Thirty'] 
values = [10, 20, 30] 

Example Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30} 
"""

keys = ['Ten', 'Twenty', 'Thirty']

values = [10, 20, 30] 

newList = [(newKeys, newVals) for i, (newKeys, newVals) in enumerate(zip(keys, values))]


print(dict(newList))