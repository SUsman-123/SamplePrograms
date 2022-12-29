#Functions
#Block of reusable code to perform specific action

def greeting():
      print("Hello")
greeting()

name=input()
greeting()
print(name)

#arguments
def greet(word):
    msg="Hello"+word
    print(msg)
name=input()
    greet(word=name)

#Problems
#Return the given arguments
def greet(arg1,arg2,arg3):
    return arg1,arg2,arg3
print(greet('Batman','Superman','Aquaman'))

#The prefild code will contain a function. write a program to concatenate the message
#"Welcom" and "Welcome HCL"
def greet(arg1,arg2):
    return arg1+arg2
print(greet('Welcome','Welcome HCL'))

#Write a program that accepts string 1,2,3,4 and it splits into list
# and returns square of each no[1,4,9,12
def greet():
    a=input()
    l1=[]
    for i in a:
        if i.isdigit():
            l1.append(int(i)*int(i))
    print(l1)
greet()
#Write a function to check if the number is divisible by 7.. Return true or false
def greeting():
    value_a=int(input())
    if value_a%7==0:
        print("True")
    else:
        print("False")
greeting()

#Write the function to return area and perimeter of a square
def greet():
    side_a=int(input())
    result=4*side_a
    print(result)
greet()

#Write the function to return second character in the word
def greet():
    val_a=input()
    for i in val_a:
        val_c=val_a[1]
    print(val_c)
greet()

#Write the function to return number of lower case and uper case letters in a string
def greet():
    low_upper=input()
    count_a=0
    count_b=0
    for i in range(len(low_upper)):
        if(low_upper[i].islower()):
            count_a+=1
        elif(low_upper[i].isupper()):
            count_b+=1
    print(count_a)
    print(count_b)
greet()

#Write a function that takes number of wins,draws and losses and
# calculate the number of points...
def matches(win_s,low_s,draw_s):
    print(win_s,low_s,draw_s)
string_a=input()
string_b=list(string_a)
win_s=0
low_s=0
draw_s=0
for i in string_b:
    if i=='w':
       win_s+=1*4
    elif i=='l':
       low_s-=-1
    elif i=='d':
       draw_s+=1*2
total=(win_s+draw_s)+low_s
matches(win_s,low_s,draw_s)

#If number is divisible by 3 it should return Macro,if a number is divisible by 5 it
#should return Polo.If it divisible by both 3 and 5  it should return MacroPolo
def greet():
    val_a=int(input())
    if(val_a%3==0 and val_a%5!=0):
        print("Marco")
    elif(val_a%5==0 and val_a%3!=0):
        print("Polo")
    elif(val_a%3==0 and val_a%5==0):
        print("Marco Polo")
    else:
        print("Please provide valid number")
greet()

#maximum of those numbers Ex:-o0d1n8--sum9 min 0 max8
def greet():
    string_s=input()
    list_a=list(string_s)
    t1=[]
    for i in list_a:
        if i.isdigit():
            t1.append(int(i))
    print(max(t1))
    print(min(t1))
    print(sum(t1))
greet()
#Factorial of a number using recursion
def recursion_fact(n):
    if n==1:
        return n
    else:
        return n*recursion_fact(n-1)
num=int(input())
if num< 0:
    print("Sorry")
elif num==0:
    print("o fact is 1")
else:
    print("The fact is",num,"is",recursion_fact(num))
















