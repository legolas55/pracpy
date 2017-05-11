#Swapping values without using a temporary variable

#traditional method
print "traditional way\n"
a=4
b=8
c=12
print "original values" ,a,b,c

temp=a
a=b
b=c
c=temp

print "swapped values" ,a,b,c,"\n"

#python tuple method
print "python way\n"
a=4
b=8
c=12
print "original values" ,a,b,c

(a,b,c)=(b,c,a)

print "swapped values",a,b,c,"\n"


#tuple extension
#packed values
(a,b,c)=(1,2,3)

f=(a,b,c)

#access by index

print "first",f[0],"second",f[1],"third",f[2],"last",f[-1]
