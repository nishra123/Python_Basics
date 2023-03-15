#Dictionary is KEY VALUE PAIRS
#denoted by {}
chintu = {}
print(type(chintu))

me= { "Monday":"Ghisai", "Tuesday":"Work", "Wednesday":"Chill", "Sunday":"Enjoy" }
#      KEY       VALUE

print(me["Sunday"])

#Dict within Dict print
me= { "Monday":"Ghisai", "Tuesday":"Work", "Wednesday":"Chill", "Sunday":"Enjoy",
      "Babu":{"All time sleep":"No Work", "Best thing to do":"Take a nap"}}

print(me["Babu"])
print(me["Babu"]["Best thing to do"])

#ADDING ELEMENTS IN DICTIONARY:
me["myself"]="Busy,do not disturb"
print(me)

#Or BY USING .update() function
me.update({"Today's breakfast":"Upma"})
print(me)

#DELETING ELEMENTS FROM DICTIONARY : USE "del" function
del me["myself"]
print(me)

#RETURNING KEYS AND VALUES    AND KEY-VALUE PAIRS    FROM DICT
#         .keys()   .values()      .items()
print(me.keys())
print(me.values())
print(me.items())

#USE OF .copy() FUNCTION
"""without .copy() fn"""
d1=me
del d1["Monday"]                 #REMOVES "Monday" BOTH FROM d1 AND me AS d1 REFERS DICT me
print(d1)
print(me)

"""with .copy() fn"""
me.update({"Monday":"Ghisai"})
d2=me.copy()
del d2["Monday"]                  #REMOVES "Monday" ONLY FROM d2 AS d2 IS NOW COPY OF DICT me
print(d2)
print(me)





