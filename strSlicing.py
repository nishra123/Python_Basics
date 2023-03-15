baburao = "Bhaarich na bhava"
print(baburao)

"""1 :  VAR NAME CAN BE ANYTHING YOU LIKE

RULES: 1)var name should not start with _, - or any no. or any special symbols.
       2)BA-LA is not allowed, BA_LA is allowed
     
        FOR RESULT JUST print(var name)"""

"""In python, INSIDE STRING, NUMBERS ARE GIVEN STARTING WITH 0 AS:
                
                B    h    a    a    r    i    c    h       n    a          b     h     a     v     a
                
                0    1    2    3    4    5    6    7   8   9    10    11   12    13    14    15    16
                
               -17  -16  -15  -14  -13  -12  -11  -10 -9  -8   -7    -6    -5   -4    -3    -2    -1    

                                                       ^               ^
Here, Empty spaces are also counted as a character"""

"""POSITIVE INDICES= START FROM NUMBERING FROM L TO R= FIRST 0
NEGATIVE INDICES= START FROM NUMBERING R TO L= FIRST -1"""
print(len(baburao))                                              #len is a function used to measure length of a string
print(len("Bhaarich na bhava"))

#to take one character from the string, use SQUARE BRACKETS[]    like,
print(baburao[4])
print(baburao[8]) #empty shown because there is a space

#to select a number of slices, we use colon inside square brackets like [a:b]

print(baburao[0:8]),        """HERE, a IS ALWAYS INCLUDING AND b IS ALWAYS EXCLUDING"""
print(baburao[-10:-7])
print(baburao[5:-1])
print(baburao[-15:15])

#sice len(baburao) is 17,
print(baburao[0:17])                            #here, result same
print(baburao[0:19937917393179])
print(baburao[0:])
print(baburao[:])
print(baburao[::])                              #here, last default is 1

print(baburao[:4])                              #here, automatically takes 0 at first


#SKIPPING CHARACTERS : ANOTHER ':'
print(baburao[0:7:2])                           #here, output is shown by skipping one character
print(baburao[0:18:3])                          #here, output is shown by skipping two characters
print(baburao[::6])                             #here, output is shown by skipping 5 characters
print(baburao[::297297297297297])               #here, first character only printed as len(str) is less

"""   [    :          :       ] KEEPING EMPTY, ONLY DEFAULT VALUES ARE SHOWN 
        ^       ^          ^
         0    STRING     DIFFERENCE
             LENGTH        DEFAULT(1)  """

"""NEGATIVE INDICES DIFFERENCE"""
print(baburao[::-2])                    #STRING ULTA, MAG DIFFERENCE


"""OTHER FUNCTIONS IN PYTHON:"""       #NO. 1 AND 2 DON'T NEED SPACES IN BETWEEN
zendu = "mast majet challay"

#1.  isalnum() : IS ALPHABETICAL OR NUMERIC?   (BOTH ALPHA OR NUMERIC ALLOWED)
print(zendu.isalnum())                #Showing false because spaces present

zendu1 = "mastmajetchallay"
print(zendu1.isalnum())              #Showing true because spaces are removed

zendu2 = "mast majet challay 123"     #showing false because numbers there, but spaces present
print(zendu2.isalnum())

zendu3 = "mast1majet2challay3"
print(zendu3.isalnum())               #Showing true because instead of spaces, numbers are added

#2. isalpha()     :   IS ALPHABETICAL?    (NO NUMERICS, ONLY APLHA)
print(zendu.isalpha())                 #Showing false because spaces present

print(zendu3.isalpha())               #showing false because spaces gone, but no.s present

print(zendu1.isalpha())              #shhowing true because spaces removed and no no.s present


#3. count()      : COUNTS A SPECIFIC CHARACTER IN STRING
print(baburao.count("a"))
print(zendu.count("l"))


#4. endswith()   : CHECKS WHETHER STRING ENDS WITH ()
print(baburao.endswith("bhava"))          #shows true
print(baburao.endswith("bhaava"))         #shows false

print(zendu.endswith("challay"))          #shows true
print(zendu.endswith("challlay"))         #shows false


#5. capitalize()  :CAPITALIZES FIRST LETTER ONLY
print(zendu.capitalize())

#6. find()      : FINDS NO. OF CHARACTER TYPED IN()
print(baburao.find("na"))

#7. lower()  ;CONVERTS ALL STRING IN LOWERCASE
#   upper()   : CONVERTS ALL STRING INTO UPPERCASE
print(baburao.lower())
print(baburao.upper())

#8. replace("a", "b") : REPLACES A WITH B
print(baburao.replace("na", "re"))
print(zendu.replace("challay", "paltay"))

