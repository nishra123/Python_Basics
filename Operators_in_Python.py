#OPERATORS IN PYTHON
"""1) ARITHMETIC
2)ASSIGNMENT
3)COMPARISON
4)LOGICAL
5)IDENTITY
6)MEMBERSHIP
7)BITWISE"""

#1)ARITHMETIC OPERATORS :
print(7  +  9)
print(7  -  9)
print(7  *  9)
print(7  /  9)                         #Divides
print(7  //  9)                        #Gives integer rounded off quotient
print(17  //  9)
print(17  %  9)                        #Gives integer remainder
print(7  **  9)                        #DOUBLE STAR OPERATOR: RAISES AFTER NO. OVER BEFORE NO.
print(2  **  3)

#2)ASSIGNMENT OPERATORS :
#ASSIGNS A PARTICULAR VALUE
x=5
x+=9
print(x)
x-=5
print(x)
x/=3
print(x)
x%=3
print(x)

#3)COMPARISON OPERATORS:
#RETURNS TRUE  OR FALSE FOR A PARTICULAR COMPARISON
i=8
print(i==5)
print(i<=5)
print(i>=5)
print(i!=5)

#4)LOGICAL OPERATORS:   GUI
#BOOLEAN ALGERBRA
a=True
b=False
print(a or b)
print(a and b)

#5)IDENTITY OPERATORS:
a=True
b=False
print(a is b)
print(a is not b)
print(5 is not 7)
print("Shreyash" is "Shreyash")

#6)MEMBERSHIP OPERATORS:
list = [1, 3, 2, 35, 326, 2727]
print(2727 in list)
print(25253 in list)

#7)BITWISE OPERATORS:
#0 - 00
#1 - 01
#2 - 10
#3 - 11
print(0 & 1)                       #& = AND == BINARY AND
print(0 | 1)                       #| = OR == BINARY ADDITION
print(0 | 3)
#MACHINE UNDERSTANDS BOOLEAN LANGUAGE FASTER






