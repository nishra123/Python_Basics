#since on last we larned that while (1) or while(True) loop lasts forever,
"""breaK = TODUN TAK"""
s=0
while (True):
    s+=1
    if s+1<7 :
        continue

    print(s)
    s+=1                   #short form of s=s+1
    if s==293:
        s+=1
        break                       #stops at 292

"""CONTINUE - Current process under 'continue' execute
Below process doesn't execute
GOES BACK TO WHILE LOOP AGAIN

WHEREAS BREAK FUNCTION COMES OUT OF A LOOP"""

