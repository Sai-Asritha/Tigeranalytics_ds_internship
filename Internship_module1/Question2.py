words=(str(input("Enter words seperated by comma")).split(','))
words.sort()
length=len(words)
j=1
for i in words:
    j=j+1
    if(j<=length):
        print(i+",",end="")
    else:
        print(i)

