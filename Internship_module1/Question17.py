email=str(input("Please enter your email for validation"))
count=0
sym="@"
dig="0123456789"
low="abcdefghijklmnopqrstuvwxyz"
spe="._"
for i in email:
    if i in sym and count==0:
        count=1
    elif count>0:
        print("invalid more than one @'s")
        break
    elif i in dig or i in low or i in spe:
        pass
    else:
        print("invalid not within conditions")
        break
