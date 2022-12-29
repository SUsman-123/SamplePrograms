#def divide_by_zero(num1,num2):
try:
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    result = num1 / num2
    print(result)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

