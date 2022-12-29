#Nested lists and strings

list_a = [5,"Six",[8,6],8,2]
print(list_a[2])
print(list_a[2][0])

list_a=["Five","Six"]
print(list_a[0][1])

#String formatting
name=input("Enter name")
age=int(input())
msg=("Hi"+name+"You are"+ str(age) +"years old.")
print(msg)

#place holder
val_1="Usman"
val_2="20"
msg="Hi{}.You are{} years old."
print(msg.format(val_1,val_2))

name="Raju"
age=-int(input())
msg="Hi{1}.You are{0}years old."
print(msg.format(name,age))


#Operation on dictiory

#add key value
dict_a={'name':'Teja','age':15}
dict_a['city']='AP'
dict_a['country']='India'
print(dict_a)

#update
dict_a['age']=24
print(dict_a)

#delete item
dict_a={'name':'usman','age':15}
print(dict_a)
del dict_a['age']
print(dict_a)

#dict.keys , dict.values, dict.items
dict_a={'name':'usman','age':15}
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

#loop over dictionary
dict_a={'name':'usman','age':23}
for key in dict_a.keys():
    print(dict_a[key])
    print(key)

dict_a = {'name': 'usman', 'age': 23}
for value in dict_a.values():
     print(value)

dict_a = {'name': 'usman', 'age': 23}
for item in dict_a.items():
     print(item)

#Converting dictionary to list
dict_a={'name':'usman','age':23}
keys_list=list(dict_a.keys())
print(keys_list)

#Converting list to dictionary
list_a=[('name','usman'),['age',23],('rool_no',54)]
print(list_a)
dict_a=dict(list_a)
print(dict_a)

#Referring same dictionary object
dict_a={'name':'usman','age':23}
dict_b=dict_a
dict_b['age']=20
print(dict_a)
print(id(dict_a))
print(id(dict_b))

#Create a copy of dictionary
dict_a={'name':'usman','age':23}
dict_b=dict_a.copy()
dict_b['age']=20
print(dict_a)
print(id(dict_a))
print(id(dict_b))

#List copy
list_a=['usman',15]
list_b=list_a.copy()
list_b.extend([30,20])

list_b.append([25,55])
print(list_b)
print(list_a)
print(id(list_a))
print(id(list_b))

#Membership of dict and clear a dict
dict_a={'name':'name','age':15}
print(len(dict_a))
if 'name' in dict_a:
    print("True")
dict_a.clear()
print(dict_a)

#Problems
#Update value of particular key
dict_a={'name':'name','age':15}
dict_a['age']=20
print(dict_a)

#remove a key --del
dict_a={'name':'name','age':15}
del dict_a['age']
print(dict_a)

#Prefilled code will contain dictonary.. write a program to update the value of given
#key-- observe
dict_a={'name':'usman','age':15,'city':'kurnool'}
dict_b=input()
dict_c=input()
dict_a[dict_b]=dict_c
print(dict_a)


dict_a={'name':'usman','age':23}
keys_list=list(dict_a.values())
print(keys_list)
#Update value of particular key

