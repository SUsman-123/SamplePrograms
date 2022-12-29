
#Set
a=2
set_a ={5,3,'hello',a}
print(set_a)
print(type(set_a))

set_a={a,[2,3]}
print(set_a)

a=1,2,3,4
set_empty = set(a)
print(set_empty)

set_c={[1,2,3]}
print(set_c)

string_a='Hola'
set_c=set(string_a)
print(set_c)


set_a = {1,2,34,44,56,77}
print(set_a[1])
print(set_a[1:3])

set_a={1,2,3,44,55,6,7}
set_a.add(7)
set_a.update([2,8])
print(set_a)
set_a.discard(7)
print(set_a)

set_a={1,2,4,6,7}
set_b={3,5,8,9,7}
union = set_a | set_b
print(union)
intersection = set_a.intersection(list_b)
print(intersection)

set_a = {1,2,4,6,7}
set_b = {3,5,8,9,7}
diff=set_a - set_b
print(diff)

set_1 ={1,2,4,5,6}
set_2 ={2,4,5}
is_subset = set_2.issubset(set_1)
print(is_subset)
is_superset = set_1.issuperset(set_2)
print(is_superset)

#Write a program to remove duplicate numbers in the list
list_a=[1,1,2,2,3,4,4]
set_1=set(list_a)
list_b=list(set_1)
print(list_b)

#Write a program to remove a list of numbers if present in the
#set.. read  inputs as comma seperated
list_a=set(input())
list_b=set(input())
list_c=set(list_b)
print(list_a-list_c)

#Given two lines of comma-seperated integers,
#Write a program to print the numbers that are presentin
#both the lines.
list_a=set(input())
list_b=set(input())
list_c=list_a & list_b
print(list_c)

#Write a program to remove in the elements other than numbers in the list.
#Ex: 1,2,3,#,5,2,@,5,7,#
list_a=list(input)
list_b=list_a.copy()
for i in range(list_a):
    if str(lisyt_a[i].isdigit()):
        print(list_b)
    else:
        list_b.remove(list_a)
    print(list_b)

list_a=list(map(str,input()))
list_b=[]
for i in list_a:
    if str(i).isdigit()==True:
        list_b.append(i)
print(list_b)
#Write a program to check superset,subset,disjoint set
set_a ={1,2,4,5,6}
set_b ={2,4,5}
is_superset = set_a.issuperset(set_b)
print(is_superset)
is_subset = set_b.issubset(set_a)
print(is_subset)
is_disjoint=set_b.isdisjoint(set_a)
print(is_disjoint)

#Write a program
string_a=input()
string_b=string_a.lower()
list_a=list(string_b)
setstr=set(list_a)
for i in setstr:
    if i!=' ':
        print(i+":",end="")
        print(list_a.count(i),end=" ")

#Write a program to print common elements in 3sets
list_a=set(input())
list_b=set(input())
list_c=set(input())
inter_sec=(list_a)&(list_b)&(list_c)
print(inter_sec)

#First line contains comma seperated integers.The second line of input will contain an
#integer (k). "5,3,7,9,5,6,2,1,8" k is 9
list_a=list(map(int,input("Enter numbers").split(",")))
kth=int(input())
list_b=[]
for i in range(len(list_a)):
    for j in range(i+1,len(list_a)):
        if(list_a[i]+list_a[j]==kth):
            list_c=[list_a[i],list_a[j]]
            list_b.append(list_c)
print(list_b)
#Read the inputs in N lines and print them as list of tuples


#perfact square
m=int(input())
n=int(input())
b=[]
for i in range(m,n):
    a=i**2
    if a<=n:
        b.append(a)
print(b)

#Write a program to rotates list D times to the left
list_a=input()
list_b=list(list_a)
number=int(input())
for i in range(number):
    t1=list_b[-1]
    list_b.remove(t1)
    list_b.insert(0,t1)
    print(list_b)

#










































































