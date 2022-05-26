row = int(input("Enter row : "))
coloum = int(input("Enter coloum : "))
k=0
for i in range(row):
    for j in range(coloum):
        print(k, end = '  ')
        k+=1
        if k>10:
            k=0
    print()