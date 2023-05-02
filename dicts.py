# this is how you make a dictionary in Python similar to an Object list in JavaScript
dog = {
    'name': "Bowser", 
    'breed': 'Frenchie', 
    'age': 4, 
    'poop_chart': {
        'M': True,
        'T': True,
        'W': True,
        'T': True,
        'F': True,
        'S': False,
        'SUN': True,
    },
    'best_friends': ['Bella', 'Taylor', 'Mikey']
}

# this for loop iterates over the keys in the dictionary.
# for key in dog.keys():
#     print(key)

# this for loop iterates over the values in the dictionary.
# for value in dog.values():
#     print(value)

# this for loop iterates over the key-value pairs in the dictionary
# for pair in dog.items():
#     print(pair)

for (key,value) in dog.items():
    print(key, '---->', value)