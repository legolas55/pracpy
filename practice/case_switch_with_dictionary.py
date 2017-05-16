#Execute appropriate peices of code in correspondence with value of a control variable


animals=[]
number_of_cats=0

def dealWithCat():
    global number_of_cats
    print "meow"
    animals.append('cat')
    number_of_cats+=1

def dealWithDog():
    print "bark"
    animals.append('dog')

def dealWithBear():
    print "yeah run"
    animals.append('bear')

# so lets say you had 3 functions you wanted to call, you can tokenDict the calls

tokenDict={
    "cat":dealWithCat,
    "dog":dealWithDog,
    "bear":dealWithBear
    }

#lets test it with some words

words=["cat","bear","cat","dog"]


for word in words:
    functionToCall=tokenDict[word]
    functionToCall()
    print "hello"


print "one liner\n"

#one line tokenDict Call

for word in words:
    tokenDict[word]() # this is adorable, +1
    
