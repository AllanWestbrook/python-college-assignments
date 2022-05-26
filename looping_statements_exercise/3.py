unit = int(input("Enter unit of power : "))
year = int(input("Enter year : "))
hel3 = int(input("Enter grams of helium 3 : "))
power = int(input("Enter power provided : "))

if (unit*year) <= (hel3*power) :
    print("yes")
else :
    print("no")