# Did you know this quirky thing about tuples?
# Creating a an empty tuple

f =()

print(f)

# creating a single item tuple

j = 4,
print (j)


# sets use {} as well but are not key value pairs like dictionaries

planets = {'Earth', 'Venus', 'Jupiter', 'Saturn', 'Saturn'}

# See duplicates get removed
print(planets)

# List Comprehension 
a = {x for x in 'abracadabra' if x in 'abcdr'}

print(a)


a = { z for z in {'Jupiter', 'Venus', 'Earth', 'Saturn','Saturn'} if z in {'Jupiter', 'Venus', 'Earth'}}

print (a)

a = {x for x in range(10) if x in range(0,12,3)}

print(a)
