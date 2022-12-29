#if
#if-else
if True:
    print("if Block")

    print("Inside if")

a=int(input())
if a>0:
    print("Positive")
else:
    print("Not Positive")
    print("End")

    #Nested conditional blocks

matches_won = int(input())
goals=int(input())
          if matches_won > 8 :
              if goals > 20 :
                print("Hurry")
            print("Winner")

#Nested conditional in else block

a=2
b=3
c=1
is_a_greatest = (a>b) and (a>c)
is_b_greatest = (b>c) and (b>a)
if is_a_greatest:
    print(a)
elif is_b_greatest :
    print(b)
else:
print(c)


number = 15
is_divisible_by_10=(number%10==0)
is_divisible_by_5=(number%5==0)
if is_divisible_by_10:
    print("Divisible by 10")
elif is_divisible_by_5:
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")


    #write a program to print the digit in the one's place

n=int(input())
x=n%10
print(x)


#Number of days (N) as input. Write a program to convert N to Years Y weeks W and Days D:
#1329=365 3+33 7+3

y=int(input())
w=int(input())
d=int(input())

list_a = list(input)
list_b = []
for i in list_a:
    if i.isdigit() == True:
        list_b.append(i)
    print(list_b)











