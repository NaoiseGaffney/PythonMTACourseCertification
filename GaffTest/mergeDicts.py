# 1. Merging Dictionaries
dictionary1 = {"name": "Joy", "age": 25, "city": "New York"}
dictionary2 = {"name": "Joy", "city": "New York", "vacation": "Spain"}
dictionary3 = {"salary": "51K"}

merged_dict = {**dictionary1, **dictionary2, **dictionary3}

print("Merged dictionary:", merged_dict)