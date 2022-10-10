sentence=input("enter word:")
vowel=['a','e','i','o','u']
count=0
for i in str(vowel).lower():
    if i in sentence:
        count+=1
if count==5:
    print("all vowels exist in given word")
else:
    print("all vowels do not exist:")
