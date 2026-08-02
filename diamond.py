rowsize=int(input("Please input the amount of rows:"))
if rowsize%2==0:
    n=int(rowsize/2)
else:
    n=int(rowsize/2)+1
space=n-1
for i in range (1,n+1):
    for j in range (1,space+1):
        print(end="")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
    print()
space=1
for i in range (1,n):
    for j in range (1,space+1):
        print(end="")
    space=space+1
    num=1
    for j in range (1,2*n-i):
        print(end=str(num))
        num=num+1
    print()
        