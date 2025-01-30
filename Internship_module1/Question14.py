valid=[1,2,5,10,20,50,100,200,500,2000]
money=int(input("enter money you want"))
n=len(valid)
for i in range(n-1,-1,-1):
    if money>=valid[i]:
        print(valid[i],"-",(money//valid[i]))
        money=money%valid[i]



