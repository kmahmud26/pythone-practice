# List

# List = [12,13,15,16]
# print(List)
# print(List[2])

# Len of A List
# List = [12,13,15,16]
# print(List)
# print(List[2])
# print (len(List))
# print(type(List))
# print(List[-1])
# print(List[2:4])
# print(List[:3])
# if 13 in List:
#     print("Yes, 13 is in List" )
# # Change a number from List
# List[2] = 20
# print(List)

# myFriends = ["Kalam","Rahim","Hadi","Tutul","Abu"]
# myFriends2 = ["Obayed","Arif","Monir","Anis"]

# myFriends[1:3] = ["Bappi","Bulbul"]
# print(myFriends)

# # Insert Name
# myFriends.insert(0,"Hasib")
# print(myFriends)
# # Append Items
# myFriends.append("Kanir")
# print(myFriends)
# myFriends.extend(myFriends2)
# print (myFriends)

# # Add elements of a tuple to a list:
# myFriends3 = ("Obayed","Arif","Monir","Anis")
# myFriends.extend(myFriends3)
# print(myFriends)

# # Remove friends
# myFriends.remove("Abu")
# print(myFriends)
# myFriends.pop(0)
# print(myFriends)
# # Print all Names
# for x in myFriends:
#   print(x)
# for x in range(len(myFriends)):
#     print(x)
# fruits = ["mango","jackfruits","Jam","Ata"]
# newlist = [x for x in fruits if "m" in x]
# print(newlist)
# newlist1 =[x for x in fruits if x!="jam"]
# print(newlist1)

# newnumber = [x for x in range(10)]
# print(newnumber)
# newnumber1 = [x for x in range(10) if x<5]
# print(newnumber1)
# newlist2 = [x.upper() for x in fruits]
# print(newlist2)
# fruits.sort()
# print(fruits)
# fruits.sort(reverse= True)
# print(fruits)
# fruits.sort(key=str.upper)
# print(fruits)   

# Dictionary
student = { 'name' : 'Khalid', 
           'Age' : 52, 
           'courses' : ["HTML","CSS"]
           
           }
# student['phone'] = '5567889-335'

# print(student.get('mobile','not found'))
# student.update({'name': 'Mahmud','Age':45})
# del student['Age']
print(len(student))

print(student.keys())
print(student.values())
print(student.items())
# student.pop('name')
print(student)
for key,value in student.items():
  print(key,value)