x,y=map(int,input().split(','))
list=[]
for i in range(x):
    sublist=[]
    for j in range(y):
        sublist.append(i*j)
    list.append(sublist)
print(list)
