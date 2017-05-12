#get a value from a dictionary and not have to handle an
#exception if the key is not in the dictionary

d={'yellow':'15'}

#ezpz

if 'blue' in d:
    print d['blue']
else:
    print 'not found'

#simpler
# here we use get to search for the key and if not found returns not found
print d.get('blue ','not found')

print d.get('yellow','not found')
