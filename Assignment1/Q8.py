
#registration problem (register only people above the age 18)

name=input("Enter the name: \n")
mbno=int(input("Enter the mobile number:\n"))
age=int(input("Enter the age:\n"))
if age<=18:
    print("Sorry! You need to be at least 18 years old to get membership.")
else :
    print(f"Congratulations {name} for your successful registration.")
