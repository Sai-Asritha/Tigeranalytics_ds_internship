word=str(input())
length=len(word)
digit="0123456789"
c1=word[0]
c2=""
count=0
for i in range(1,length):
    if word[i] in digit:

        count+=int(word[i])
        i+=1
    if count==9:
        c2=word[i]
        print(c1,c2)
        c1=c2
        count=0



