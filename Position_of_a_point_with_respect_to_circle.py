#program to tell about arbitary point lie with in the circle ,on the circle,outside the  circle
x=int(input ('enter the x cordinate of centre'))
y=int(input('enter the y cordinate of centre '))
r=int(input('enter the radius of a circle'))
x1=int(input('enter the x cordinate of arbitary point'))
y1=int(input('enter a y cordinate of arbitary point'))
d=(((x1-x)**2)+((y1-y)**2))*0.5;
if r>d:
    print('with in the circle')
elif r<d:
    print('outside the circle')
else:
    print('on the circle')
#program ends

