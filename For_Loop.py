list0= [ "Abhijeet", "Ketan", "Omkar", "Mi"]
for item in list0:
    print(item)

list1= [["Abhijeet",10] , ["Ketan",4], ["Omkar", 9], ["Mi", 6]]
for item, panipuri_plate in list1:
    print(item, panipuri_plate)
    print(item,"and ate this much panipuri plate:",panipuri_plate)

dict1=dict(list1)
print(dict1)

#While using Dictionary and using multiple variables in a loop , .items() is must
for items,panipuri_plate in dict1.items():        #Otherwise shows error
    print(items,panipuri_plate)

#Otherwise for a single variable:
for item in dict1:
    print(item)

something=["Babu", "Shona", "Sanky", 3 ,2543, 535, 215, 36]
for items in something:
    if str(items).isnumeric() and items>=7:              #Here, typecasting str(items) is important otherwise shows error
        print(items)

        
