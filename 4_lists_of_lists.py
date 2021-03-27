

list_1 = [20,10,5,15,30]
list_2 = [20,10,5,15,30,20]
list_3 = [20,10,30]
list_4 = [20,10,5,15]
list_5 = [40,30]
outter_list = [list_1,list_2,list_3,list_4,list_5]

counter = 1

for val in outter_list:
    print("List "+str(counter))
    total = 0
    for item in val:
        total += item
    print(str(total))
    counter+=1