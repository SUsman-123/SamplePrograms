# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("hello")
print("Hello world")
print("25x10")
print("Hello " + "Usman")

#Print addition of multiple numbers
a = 10
b = 20
c = 30
print(a+b+c)

#Print length of string
s ="Hello"
print(len(s))

#Print Python is Amazing", using tab space and new line characters
print("Python\tis\tAmazing")

#Read two strings in two different variables, concat them and print
s1 = "Hello "
s2 = "World"
print(s1+s2)

#Print remainder, quotient of the division. print- both integer and
x=10
y=2
print(x/y)
print(x//y)
#Types of different variables
print(type(x))
print(type(y))
print(type(s))

#data types in python
x1=10
print(type(x1))
x2=10.5
print(type(x2))
x3="Hello"
print(type(x3))
myList=["apple","ball","cat"]
print(type(myList))
myTuple=(1,2,3,4,5)
print(type(myTuple))
mySet={"Hello ","My name is ","Usman"}
print(type(mySet))
thisDict={"brand": "Ford","Model": "Mustang","Year":1994}
print(type(thisDict))



alpha='abcdefghijklmnopqrstuvwxyz'

print(list(alpha))
print(tuple(alpha))
print(set(alpha))


print(id("hello"))

# referring the same object
list_a=[1,2,3,5]
list_b=list_a
print(id(list_a))
print(id(list_b))

list_b[3]=4
print(list_a)
print(list_b)
#compound assignment example
list_a=[1,2]
list_b=list_a
list_a=list_a+[6,7]

print(str(list_a))
print(str(list_b))

list_a=[1,2]
list_b=list_a
list_a+=[6,7]

print(str(list_a))
print(str(list_b))

list_a=[1,2]
print(list_a)
list_b=[3,list_a]
list_a[1]=4

print(list_a)
print(list_b)

#Splitting a string
#str_var.split(separator), default seperator is whitspace
#multiple whitespaces are considered as single whitespaces
numbers="123    4"
num_list=numbers.split()
print(num_list);

numbers="1,2,34"
num_list=numbers.split(',')
print(num_list)

numbers="1   2 3 4"
num_list=numbers.split(" ")
print(num_list)

string_a="Python is astonishing"
list_a=string_a.split('a')
print(list_a)

list_a=['Python is','progr','mming l','nug','ge']
string_a="a".join(list_a)
print(string_a)

list_a= list(range(4))
print(list_a)

list=['a','b','c','d','e','f']
list1=list[0:3]
list2=list[3:6]
print(list1)
print(list2)
list3=list[-1:-5:-2]
print(list3)
list7=list[0:6]
print(list7)
list5=list[::-2]
print(list5)

m="hello "
n=5
print(m*n)
#Static way
m="5 "
n=3
print(m*n)

m="Usman"
n=3
print(n*m)

m="Apple"
n="apple"
print(m==n)

m="apple"
n="apple"
print(m==n)

m="AppLe"
n="ApplE"
print(m==n)
print("ABC" == "ABC")
print("ABC" !="CBA")
print("abc" == "ABC")


list_a=[1,5,6]
list_b=[5,4,7]
print(list_a[0] < list_b[2])

n1=input()
n2=input()
print(n1[0]<n2[-1])

print("abc" == "ABC")

m1=int(input())
p1=int(input())
c1=int(input())
print((m1>=70 and p1>=60 and c1>=60))
print(m1+p1+c1>=180)

#slicing
a="Waterfall"
part = a[1:6:3]
print(part)

#isdigit
is_digit ="4748".isdigit()
print(is_digit)

#strip

mobile = "987697647"
mobile = mobile.strip()
print(mobile)


#swap case
str1="PyThOn"
print(str1.swapcase())

#convert dd-mm-yy format to dd/mm/yy
x="10-20-2022"
print(x)
y=x.replace("-","/")
print(y)

#Polindrome

pol="1221"
print(pol[::-1]==pol)

# Valid password

name =input()
cap_count = 0
small_count = 0
spec_count = 0
num_count = 0
for ele in range(len(name)):
    if(cap_count==0):
        if(name[ele].isupper()):
            cap_count+=1
        if(small_count==0):
            if(name[ele].islower()):
            small_count+=1
        if(spec_count==0):
            if(name[ele]=="@"):
               spec_count+=1
            if(num_count==0):
                if(name[ele].isdigit()):
                    num_count+=1
        if(cap_count==1 & small_count==1 & spec_count==1 & num_count==1):
            print("Strong password")
        else:
            print("Not strong")
