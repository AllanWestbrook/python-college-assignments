a = int(input("Enter large num 1 : "))
b = int(input("Enter small num 2 : "))

while(True):
    rem = a%b
    a,b = b,rem
    
    if rem == 0:
        break
    
print(a)
