print("Right angle triangle made out of (*)")
n=int(input("Please input the amount of rows:"))
for i in range(n):
    for j in range(i+1):
        print("*" ,end="")
    print()