x,y=0,0
path=str(input()).split(',')
for i in path:
    p=0
    length=len(i)
    temp=""
    if i[p]=='U':
        p+=2
        while p<length:
            temp+=i[p]
            p+=1
        y+=int(temp)
    elif i[p]=='D':
        p+=4
        while p<length:
            temp+=i[p]
            p+=1
        y-=int(temp)
    elif i[p]=='R':
        p+=5
        while p<length:
            temp+=i[p]
            p+=1
        x+=int(temp)
    elif i[p]=='L':
        p+=4
        while p<length:
            temp+=i[p]
            p+=1
        x-=int(temp)
res=((x**2)+(y**2))**0.5
print(res)

