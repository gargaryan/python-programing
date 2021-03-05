row=int(input(''))
for i in range(0,row):
    for j in range(row,i,-1):
        print("*",end=" ")
    for k  in range(i+1):
        print(' ',end=" ")
    for l in range(i):
        print(' ',end=" ")
    for m in range(row,i,-1):
        print('*',end=" ")
    print('')
#First loop ends
for i in range(0,row):
    for j in range(i+1):
        print('*',end=" ")
    for k in range(row,i,-1):
        print(' ',end=" ")
    for l in range(row,i+1,-1):
        print(' ',end=" ")
    for m in range(i+1):
        print('*',end=" ")
    print('')
#second loop ends
________________________________________________________________________________________________________________________________________________________________
* * * * *  * * * * *
* * * *      * * * *
* * *          * * *
* *              * *
*                  *
*                  *
* *              * *
* * *          * * *
* * * *      * * * *
* * * * *  * * * * *
________________________________________________________________________________________________________________________________________________________________
