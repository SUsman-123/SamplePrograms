#Printing statement
s="Hello"
s1='Hello'
print(s1)
print(s)
print("Abc")

#Relational operator in string
s1="Hello"
s2="World"
print(s1==s2)
#Single statement
print("Hello"=="World")
print("ABC"=="ABC")
print("ABC"=="abc")

#Method 1 Print addition of multiple numbers

list_a=[10,20,30,40]
sum=0
for i in range(0,len(list_a)):
    sum=sum+list_a[i]
print("sum of all elements in given list:",sum)
# Method 2
my_list=[10,20,30,40]
total=sum(my_list)
print("sum of all elements in given list:",total)

#Print length of a string
str="Usman"
print("Length of a string is",len(str))

#Print "Python is Amazing",use tab space and new line characters
print("Python\tis\tAmazing")

#Read two strings in two different variables,concate them and print length of concated string
str1="shaik"
str2="usman"
result=str1+str2
print(result)
print(len(result))

#Print remainder,quotient of the division.print both integer and flot results
rem=10
quo=5
result=rem/quo
print(int(result))
print(quo)

#print type of various kind of variables
var1="Hello"
var2=10
var3=10.5
od=OrderedDict()
print(type(var1))
print(type(var2))
print(type(var3))
print(type(od))













