### Using lambda to return a function

def make_lambda(n):
    return lambda x: (x+n)**2

lambda_object = make_lambda(12)

print (lambda_object(12))

### Using Lambda as an argument

lambda_map = map( lambda h: h*7, [ i for i in range (10)])

print(list(lambda_map))

#Create list using regular way

riches = []

for x in range(50):
    riches.append(x**2)

print(riches)

#One Liner using list comprehension

riches = [x**3 for x in range (50)]

print (riches)


#lambda + list comprehension + maps

riches = list(map(lambda x:x**4, range(10)))

print(riches)


#### A list comprehension consists of brackets containing an
### expression followed by a for clause, then zero or more for
### or if clauses. The result will be a new list resulting
### from evaluating the expression in the context of the for and if clauses which follow it.


hello = [(i,j) for i in [1,2,3] for j in [1,2,6] if i ==j]

print(hello)

hello2 = [ (i,j,k) for i in [1,2,3,4] for j in ['a','b','c','d'] for k in ['!','@','$','%'] if i != j and j != k]


print(hello2)



