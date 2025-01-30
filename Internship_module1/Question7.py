transactions=str(input()).split(',')

withdraw=0
dep=0
tot=0
for i in transactions:
    temp=""
    x=0
    length=len(i)
    if i[x]=='D':
        x+=1
        while x<length:
            temp+=i[x]
            x+=1
        dep+=int(temp)
    elif i[x]=='W':
        x+=1
        while x<length:
            temp+=i[x]
            x+=1
        withdraw+=int(temp)


tot=dep-withdraw
print(tot)




