#implementing the nCr
#formula nCr=(n-1)C(r-1)+(n-1)r
#C(n,r)=C(n-1,r-1)+C(n-1,r)
def combination(n,r):
    if(r>n):
        return 0
    elif (r==0 or r==n):
        return 1
    return combination(n-1,r-1)+combination(n-1,r)
result=combination(int(input("Enter a N value:")),int(input("Enter a  R value:")))
print(result)
