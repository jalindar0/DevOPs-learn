thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  1:1111
}

#print(thisdict.get("brand"))
#print(thisdict["brand"])
'''
for key in thisdict:
    value = thisdict[key]
    print(key, ":", value)
    '''
'''
  You can use the items() method to get both keys and values together as tuples.
for key, value in thisdict.items():
    print(key, ":", value)'''

 #   If you only need to access the values without the keys, you can use the values() method.
#python

#for value in thisdict.values():
#   print(value)

#Changeable
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Duplicates Not Allowed


#Dictionaries cannot have two items with the same key,Duplicate values will overwrite existing values

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "price":2
}
print(len(thisdict))

'''
'''
thisdict = dict(name = "John", age = 36, country = "Norway")
thisdict = dict()
print(thisdict)
'''


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "price":2
}
#print(thisdict.keys())    #dict_keys(['brand', 'model', 'year', 'price'])
#print(thisdict.values())  #dict_values(['Ford', 'Mustang', 2020, 2])
#print(thisdict.items())   #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020), ('price', 2)]) 

'''
my_dict = {"a": 1, "b": 2, "c": 3}

# Get a view of the dictionary's keys
keys_view = my_dict.keys()

# Iterate over the keys
for key in keys_view:
    print(key)

# Modify the dictionary
my_dict["d"] = 4

# The view reflects the change
for key in keys_view:
    print(key)
'''