n=int(input("Please input the number of rows:"))
number=1

print("Floyd's triangle")
for i in range (1, n+2):
    for j in range (1, i+2):
        print(number, end="")
        number=number+2
    print()
