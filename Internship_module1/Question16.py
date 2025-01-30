player1=0
player2=0
while player1<=5 or player2<=5:
    p1=str(input("player1:"))
    p2=str(input("player2:"))
    if p1==p2:
        print("DRAW")
    elif p1=="stone" and p2=="paper" or p1=="paper" and p2=="scissor" or p1=="scissor" and p2=="stone":
        print("Player B wins")
        player2+=1
    elif p1=="stone" and p2=="scissor" or p1=="paper" and p2=="stone" or p1=="scissor" and p2=="paper":
        print("Player a wins")
        player1+=1


