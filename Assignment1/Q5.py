
#program to calculate the simle interest
pamt,rate,time=int(input("Enter the principal amount\n")),float(input('Enter the rate of interest\n')),int(input("Enter the time(years)\n"))
print(f"Simple interest is {(pamt*rate*time)//100}")