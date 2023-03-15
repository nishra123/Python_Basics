a=5
b=6
c=sum((a,b))            #BUILT-IN FUNCTION - USE ctrl and click on any builtin func in Pycharm to get info
print(c)

#USER DEFINED FUNCTIONS:
def function1():
    print("Hello you are in function1 for now")

print(function1())                     #parentheses is necessary inside
#since there is no RETURN assigned, it returns NONE also

function1()           #directly prints function1

def function2(a,b):
    print("THODA ABHYAS KARUN FIT RAHA BE", a+b )
    return a*b
print(function2(3,9))                          #NOW IT PRINTS BOTH 12(AS A RSULT OF PRINT FN) AND 27(AS A RESULT OF RETURN)
function2(6,7)

def function3(a,b):
    """This is a function which calculates mean of two numbers
    this function doesn't work for three or more numbers"""           #The first line written in """""" next after a function is defined is called a DOCSTRING
    mean=(a+b)/2
    print(mean)
    return(mean*100)

s=function3(68,237)
print(s)
print(function3.__doc__)

#DOCSTRINGS ARE VERY MUCH USEFUL AND NECESSARY WHEN YOU HAVE A CODE WITH MANY CLASSES, FUNCTIONS AND MANY THINGS ARE GETTING IMPORTED

#FOR COMPLEX USERR DEFINED FUNCTIONS, IT IS MUST TO WRITE A DOCSTRING
# TO PRINT A DOCSTRING, use print(function.__doc__)
"""                                       ^ Here function name without parentheses"""

#USER DEFINED FUNCTION START AT def AND END AT return



