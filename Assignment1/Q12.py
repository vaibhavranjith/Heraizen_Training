#calculate discount for a purchase based on poscession of membership card

bamt=int(input("Enter the bill amount\n"))
if input("Do you have a membership card?:\n") =='Y':
    print(f"Thank you! Your total bill amount is Rs {bamt}, discount is Rs {bamt*0.1} and net amount payable is Rs {bamt*0.9}")
else :
    print(f"Thank you! Your total bill amount is Rs {bamt}, discount is Rs {bamt*0.03} and net amount payable is Rs {bamt*0.97}")