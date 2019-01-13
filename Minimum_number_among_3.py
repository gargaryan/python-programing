#program  to find minimum of three number
num1=int(input('enter a first number'))
num2=int(input('enter a second number'))
num3=int(input('enter a thitd number'))
if num1<num2 and num1<num3:
    print(num1,'is minimum number')
elif num2<num3:
    print(num2,'is minimum number')
else:
    print(num3,'is minimum number')
#program ends
    
