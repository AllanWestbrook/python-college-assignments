import random

x =  random.randrange(0,100,1)
n=0
while (n<4):
    
    g = int(input("Enter guess : "))
    if x == g :
        print("You guessed it right!!")
        break
    
    elif x > g :
        if x - g >= 10 :
            print("Much higher")
            n += 1
        else :
            print("higher")
            n += 1
    
    else :
        if g - x >= 10 :
            print("Much lower")
            n += 1
        else :
            print("lower")
            n += 1

else:
    print("Sorry your num is",x)