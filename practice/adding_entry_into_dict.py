#add an entry into a dictionary

#look before you leap
import collections 

index={}


def addEntry(word,param):
    if word in index:
        index[word].append(param)
    else :
        index[word]=[param]

addEntry("red",12)

print (index)

addEntry("yellow",14)

print (index)

addEntry("red",18)

print (index)


#easier to get permisson

index={}

def addEntryPerm(word,param):
    try:index[word].append(param)
    except KeyError: index[word]=[param]

addEntryPerm("sand",123)
print (index)

addEntryPerm("sand",1234)
print (index)


#setdefault
index={}

def addword(word,param):
    index.setdefault(word,[]).append(param)

addword("sandy",777)
print (index)

addword("sandy",888)
print (index)

#even simpler
data={("one",7),("one",8)}
index=collections.defaultdict(list)

for (key,value) in data:
    index[key].append(value)

print (index)





