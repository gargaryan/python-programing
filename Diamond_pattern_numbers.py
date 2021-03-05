sample_input=int(input(''))

row=(sample_input//2)+1
ctr=1
ctr1=1
ctr2=row-1
for i in range(0,row):
    for j in range(row,i,-1):
        print(" ",end=" ")
    for k in range(ctr,0,-1):
        print(k,end=" ")
    ctr+=1
    for l in range(2,ctr):
        print(l,end=" ")
    ctr1+=1
    print('')
# first loop ends
ctr3=row
for i in range(1,row):
    for j in range(0,i+1):
        print(" ",end=" ")
    for k in range(ctr2,0,-1):
        print(k,end=" ")
    ctr2-=1
    for k in range(2,ctr3):
        print(k,end=" ")
    ctr3-=1
    
    
    print('')
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
        
Input : 5
Output :
  1
 212
32123
 212
  1

Input : 7
Output :
   1
  212
 32123
4321234
 32123
  212
   1     
    
    
    
