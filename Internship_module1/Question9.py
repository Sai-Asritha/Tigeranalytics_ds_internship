l1=[]
while 1:
    tup=input()
    if not tup:
        break
    name,age,score=tup.split(',')
    l1.append((name,int(age),int(score)))
sort_list=sorted(l1,key=lambda x:(x[0],x[1],x[2]))
print(sort_list)

