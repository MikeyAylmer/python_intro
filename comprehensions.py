nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# so if we wanted to create a new list of just evens without list comprehensions we would do something like this.

# evens = []
# for n in nums:
#     if n % 2 == 0:
#         evens.append(n)

# print(evens)

# # ^ here we write a loop then a conditional and then we push to the new array/list


# evens = [num for num in nums if num % 2 == 0] # So this reads, num for num in nums if num is even
# here we are creating a new list with the [square brackets] and then filling it with content based off of nums.
#  note there is as loop in there along with a conditional.

# to double everything we start with new list brackets [] then we loop. we come up with some variable name
# like num or whatever, and then what we need to do is specify that we want to double each number,
doubles = [num * 2 for num in nums ]
# same as 
# doubles = []
# for num in nums:
    # doubles.append(num * 2)

# so basic syntax is this what we want to add, for thing, in list.
# [what_to_append for thing in list]

values = [2,4,6,8]
[value * value for value in values]

# we could also use list comprehensions to create something like a game board where we have nested list/arrays
# example[[0,1,0],[1,1,1], [0,0,0]] if we wanted to create this, or write a function to create a 3x3, 4x4, or 5x5 board.
# we could use nested list comprehensions
# you can start with this [[] for x in range(3)] = [[],[],[]]
# and then do [[0 for y in range(3)] for x in range(3)]

def make_board(size, initial_val=None):
    return [[initial_val for value in range(size)] for board in range(size)]

dogs = [
    {'name': 'bowser', 'breed' : 'frenchie'},
    {'name': 'bella', 'breed' : 'frenchie'},
    {'name': 'tazz', 'breed' : 'english'},
    {'name': 'lexus', 'breed' : 'english'},
    {'name': 'oscar', 'breed' : 'frenchie'},
    {'name': 'tiny', 'breed' : 'frenchie'},
]

# here we loop through each animal in dog and then add the animal['name']
pets = [animal['name'] for animal in dogs]
# so for each animal in the dog list, we want to create a new list with that animals names.

# and if we just wanted a specific breed we could do this and set the conditional to equal 'frenchie'.
frenchies = [animal['name'] for animal in dogs if animal['breed'] == 'frenchie']

# we can also add in a else along with the if conditional.
scores = [55, 89, 99, 87, 60, 70, 74, 76, 90, 50, 82]
# grades = ['PASS' for score in scores]
grades = ['PASS' if score >= 70 else 'FAIL' for score in scores]

# the syntax is read like this
# [do_this if something else do this for thing in things]