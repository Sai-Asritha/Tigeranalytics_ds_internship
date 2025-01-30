ip1=int(input("choose 1 or 2"))
ip2=str(input())
ip3=int(input())
while ip3>0:
    if ip1==1:
        temp=ip2[0]
        length=len(ip2)
        x=""
        for i in range(1,length):

            x+=ip2[i]

        x+=temp
        print(x)
        ip2=x

    elif ip1==2:

        length=len(ip2)
        temp=ip2[length-1]
        x=""
        x+=temp
        for i in range(0,length-1):

            x+=ip2[i]

        print(x)
        ip2=x
    ip3-=1

