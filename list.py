party = ["Balaji Chips", "Sprite", "Kurkure", "Maaza"]
print(party)

#items in a list can also iclude an integer like:
party1 = ["Balaji Chips", "Sprite", "Kurkure", "Maaza", 92797, 6262626262626262]
#              0            1          2            3     4           5
print(party1)

#JUST LIKE THE PREVIOUS CASES:
print(party1[0])              #prints 'Balaji chips'
print(party1[-1])             #prints '6262626262626262'
print(len(party1))
#print(party1[6])              #SHOWS ERROR AS NO NO.6 ELEMENT IS PRESENT

numbers=[218, 277, 288, 212, 1]
print(numbers)
print(numbers[-2])

#PYTHON LIST FUNCTIONS::::::

#SORTING NUMBERS

#1)   .sort()
numbers.sort()               #SORTS LIST ITEMS IN ASCENDING ORDER
print(numbers)

#2)     .reverse()
numbers.reverse()
print(numbers)              #SORTS LIST ITEMS IN DESCENDING ORDER

#3)     .append()           #APPEND= JOIN/ADD AT LAST
numbers.append(82)
print(numbers)
#You can apply append function as many times as you like; EG.
newday= []                                  #Khali List
newday.append(1)
newday.append(14)
newday.append(14)
newday.append(199)
print(newday)

#4)         .insert(i,_)      #inserts desired value AFTER ith INDEX
numbers.insert(0,7272727272727272)
numbers.insert(-1, 828)
numbers.insert(3, 1234)
print(numbers)

#5)        .remove()          #Removes a specific value
numbers.remove(7272727272727272)                        #removes 7272727272727272
#numbers.remove(198927272989817272)                      #SHOWS ERROR BCOZ 198282983081081308 NOT PRESENT IN LIST TO REMOVE
numbers.remove(288)                                     #removes 288

#6)      .pop()              #removes LAST ELEMENT FROM LIST
numbers.pop()
print(numbers)                                        #LAST ELEMENT 82 IS REMOVED

#7) TUPLE ()  : # ():PARENTHESIS    []:SQUARE BRACKETS   {}:CURLY BRACKETS

#TUPLE OR USING PARENTHESIS DOESN'T ALLOW TO CHANGE ANY ELEMENT

#TUPLE = ()    AND LIST = []
joe = (5 , 22, 24)
#joe[1]=290                    #SHOWS ERROR AS IN TUPLES, VALUES OF AN ELEMENT CANNOT BE CHANGED

baburao= (1)            #Shows only 1
print(baburao)
baburao= (1,)           #NOW IT FORMS A TUPLE
print(baburao)

#FOR TUPLE OF SINGLE ELEMENT, PUT A COMMA AFTER IT AS (I,)

"""SWAPPING VALUES OF TWO VARIABLES/INTERCHANGING TWO VARIABLES"""
#GENERAL TECHNIQUE
a=1
b=2
something=a
a=b
b=something

print(a,b)

#PYTHON TECHNIQUE      #IN-BUILT PYTHON FUNCTIONS
a,b = b,a
print(a,b)