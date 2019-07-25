#dictionary that maps each key to multiple values


# works but duplicate values with the same key occurs
d1={}
d1.setdefault("yellow",[]).append(1)

print (d1)

d1.setdefault("yellow",[]).append(1)

print (d1)

d1.setdefault("yellow",[]).append(1)
d1.setdefault("green",[]).append(1)
print (d1)


#no duplicates
d2={}

d2.setdefault("hello",{})[6]=1
d2.setdefault("hello",{})[6]=1
d2.setdefault("hello",{})[5]=1
d2.setdefault("green",{})[5]=1

#dictionary has its own copy method
d3=d2.copy()
d4=d2.copy()

print ("the original dictionary", d2)

#removing a value associated with a key
del d2["hello"][6]

print ("removing a value of a key", d2)

#removing a key

del d2["hello"]

print ("removing a key entirely",d2)

#clearing a dictionary

d2.clear()

print ("clearing a dictionary", d2)

print ("d3 looks like this", d3)

# delete a random item

d3.popitem()
print ("pop a random item", d3)


#delete a specific item
d3.pop("hello")

print ("Pop hello from the dictionary",d3)




