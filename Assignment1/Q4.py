#program to swap two numbers

a,b=int(input("Enter the num1\n")),int(input("Enter the num2:\n"))
print(f"Before the swap,the values of num1={a} and num2={b}")
a,b=b,a
print(f"After the swap, the values of num1={a} and num2={b}")