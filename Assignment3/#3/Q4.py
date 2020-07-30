# Q4
vowels=["a","e","i","o","u"] 
word=input("Enter a word: ")
print(len(list(filter(lambda ele: ele in vowels,list(word)))))