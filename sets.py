lemon = {'sour', 'yellow', 'fruit', 'bumpy'}
banana = {'fruit', 'smooth', 'sweet', 'yellow'}
orange = ['fruit', 'bumpy', 'orange', 'sweet']

# there is a union built in set method that unites the sets.
# banana | lemon = {'bumpy', 'fruit', 'smooth', 'sour', 'sweet', 'yellow'}

# intersection is a built in set method that returns whatever values match in the given sets.
# lemon & banana = {'fruit', 'yellow'}

# Difference built in set method returns whatever is in the first set that is not in the second set.
# lemon - banana = {'bumpy', 'sour'}
# ORDER of set also matters
# banana - lemon = {'smooth','sweet'}

# symmetric_difference is a built in set method that returns both differences 
# banana ^ lemon =  {'bumpy', 'smooth', 'sour', 'sweet'}

# we can also loop over a set into a list like this.
# for adj in banana:
#     print(adj)
# = fruit, yellow, smooth,sweet

# you can also use union with it like this.
for adj in banana | lemon | set(orange):
    # since orange is a list we use set() to turn it into set.
    print(adj)