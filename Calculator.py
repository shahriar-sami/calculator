print("The operators you can use\n + \n - \n / \n * ")
print("enter your first number")
num1 = int(input())
print("enter your second number")
num2 = int(input())
print("enter your operator")
num3 = input()

if num3 == '+':
    sum1=num1 + num2
    print(sum1)
elif num3 == '-':
    sum2 = num1 - num2
    print(sum2)
elif num3 == '/':
    sum3 = num1 / num2
    print(sum3)
elif num3=='*':
    sum4 = num1 * num2
    print(sum4)
else:
    print("Operator is not found")                