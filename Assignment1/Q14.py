#grades average and total marks
s1,s2,s3=int(input("Enter the marks scored in 1st subject:\n")),int(input("Enter the marks scored in 2nd subject:\n")),int(input("Enter the marks scored in 3rd subject:\n"))
average=(s1+s2+s3)/3
Grade=("C" if average<=35 else ("B" if average<=60 else "A"))
print(f"Total marks: {s1+s2+s3}\nAverage: {average}\nGrade: {Grade}")