
bamt=int(input("Enter the billing ammount:\n"))
print(f"Your net billing amount: {bamt if bamt<=6000 else bamt*0.9}")
