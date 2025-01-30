low,high=map(int,input("enter range inclusive to find even numbers").split(','))
for i in range(low,high+1):
    if(i%2==0 and i<high):
        print(i,end=",")
    elif i%2==0:
        print(i)
