sum1=0
count1,count2,count3=0,0,0
for i in range(0,8):
    a=int(input("Num : "))
    
    if a == 0:
        count1+=1
    elif a>0:
        count2+=1
    else:
        count3+=1
    
    sum1+=a

print("sum = ",sum1)
print("Zero = ",count1)
print("Positive = ",count2)
print("Negative = ",count3)