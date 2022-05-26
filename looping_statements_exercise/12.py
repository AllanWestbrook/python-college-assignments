import random
n=0
w,l,t = 0,0,0
while n<5 :

    x = random.randrange(0,4,1)
    us = int(input("rock(1), paper(2) or scissor(3) : " ))
    
    if us == x :
        print("its a tie")
        t+=1
        
    elif us == 1 :
        if x == 3 :
            print("Rock wins over scissors")
            w+=1
        else:
            print("You lose")
            l+=1
            
    elif us == 2 :
        if x == 1 :
            print("Paper wins over rock")
            w+=1
        else:
            print("You lose")
            l+=1
            
    elif us == 3 :
        if x == 2 :
            print("Scissors wins over paper")
            w+=1
        else:
            print("You lose")
            l+=1
            
    n+=1
    
print("Wins = ",w)
print("Ties = ",t)
print("Loses = ",l)