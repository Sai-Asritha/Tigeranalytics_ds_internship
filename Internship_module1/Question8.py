passwords=str(input("Enter list of passwords:")).split(',')
low="abcdefghijklmnopqrstuvwxyz"
upp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spec="$#@"
num="0123456789"
res="a"
for i in passwords:
    length=len(i)
    l=u=s=n=0
    if length<6 or length>12:
        continue
    for j in i:
        if j in low:
            l+=1
        elif j in upp:
            u+=1
        elif j in num:
            n+=1
        elif j in spec:
            s+=1
    if l>=1 and u>=1 and n>=1 and s>=1:
        res=i
        break
print(res)

