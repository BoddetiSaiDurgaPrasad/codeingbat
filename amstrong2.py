import math
x = int(input())
a=x
temp =x
y=0
ln = len(str(x))
rem=0
"""while(x>0):
    len +=1
    x= x//10"""
while(a>0):
    rem=a%10
    a=a//10
    y = y+ rem**ln
if(temp==y):
    print("amstrong")
else:
    print("Not a amstrong ")
