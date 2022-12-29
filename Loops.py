#While
a=int(input())
counter=0
while counter<3:
    a=a+1
    print(a)
    counter=counter+1
    a=int(input())
    while counter<3:
        a=a+1
        print(a)
        counter =counter+1
        print("end")

#Sum of given numbers

list_a=[10,20,30,40]
sum=0
for i in range(len(list_a)):
    sum=sum+list_a[i]
print(sum)
#Sum of product
sum1=1
for i in range(1,5):
    sum1=sum1*i
print(sum1)
print("\n")

#Print Rightangle traingle pattern

for i in range (1,4):
    for j in range (1,i+1):
        print(" * ",end="")
    print()
print("\n")

for i in range(1,4):
    for j in range(1,i+1):
        print(end=" ")
        for k in range(1,j+1):
            print("* ",end="")
    print()


#square box

for i in range(1,5):
    for j in range(1,5):
        print("* ",end="")
    print()

for i in range(1,4):
    for j in range(1,i-1)8
        print("* ", end="")
    print()
#Right side traingle
n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end='')
    for k in range(i):
        print("*",end='')
    print()

n=int(input())
for i in range(n):
    for j in range(n-i+1)
        print("",end='')
        if i


