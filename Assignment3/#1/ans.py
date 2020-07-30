def ask(d):
    print("Question "+ d["qno"])
    print(d["question"])
    print("1)"+d["opt1"])
    print("2)"+d["opt2"])
    print("3)"+d["opt3"])
    print("4)"+d["opt4"])


qfile=open("D:/python/Assignment3/#1/quiz.txt.txt","r")
cont=qfile.readlines()
quiz=[]
i=0
while i<len(cont):
    qno=cont[i]
    question=cont[i+1]
    opt1,opt2,opt3,opt4=cont[i+2],cont[i+3],cont[i+4],cont[i+5]
    ans=cont[i+6]
    quiz.append({
                    "qno":qno,
                    "question":question,
                    "opt1":opt1,"opt2":opt2,"opt3":opt3,"opt4":opt4,
                    "ans":ans
            })
    i+=7
nqc=0
nqw=0
perc=0
result=0
for q in range(len(quiz)):
    ask(quiz[q])
    print("-"*30)
    opt=input("Enter option [1-4]: ")
    if(opt==quiz[q]["ans"][4]):
        nqc+=1
    else:
        nqw+=1

print(f"The number of correct answers: {nqc}")
print(f"The number of wrong answers: {nqw}")
print(f"Percentage marks: {(nqc*100)/(nqc+nqw)}")
print(f"Result: {nqc} / {nqc+nqw}")
qfile.close()
