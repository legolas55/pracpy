#how to construct a dictionary without having to quote the keys

#tradtional way

data={'red':23,'green':45,'blue':87}

print data

# why dont we just make a dictionary creator 
def createDict(**kwargs):
    return kwargs

#call it and store into data
data=createDict(red=1,green=2,blue=3)

print data

#but I want more!


def createDictMorePower(*args,**kwds):
    yesthislist={}
    for k,v, in args:yesthislist[k]=v
    yesthislist.update(kwds)
    return yesthislist

#pass in data as an args input
boom=createDictMorePower(*data.items(),orange=1,veort=15,purple=30)
#so see we can pass in args and keyword args

print boom

#yeah lets make it simpler

def simple(*args,**kwds):
    d=dict(args)
    d.update(kwds)
    return d

#pass in boom as an args input
boom2=simple(*boom.items(),freemoney=1)

print boom2




