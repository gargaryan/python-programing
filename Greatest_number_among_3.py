#program to find a greatest of three number
num1=int(input('enter a first number'))
num2=int(input('enter a second number'))
num3=int(input('enter a third number'))
if num1>num2 and num1>num3:
    print(num1,'is the greatest number')
elif num2>num3:
    print(num2,'is greatest number')
else:
    print(num3,'is greatest number')


#program ends
