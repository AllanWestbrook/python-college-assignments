cost = 100

while(True):
    act = input("Actual : ")
    cho = input("Choice : ")
    if(act==cho):
        cost+=9
    else:
        cost-=10
        
    if cost>=200 or cost<=0 :
        break

print(cost)