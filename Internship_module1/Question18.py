
    #Qd
n = int(input("Qd"))

for i in range(n):
    if i == 0:
        print("***")
    elif i == n // 2:
        print("* ***")
    elif i == n - 1:
        print("* * *")
    elif i > n // 2:
        print("* *")
    else:
        print("*")
#Qe
    n = int(input("Qe"))

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == n // 2:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()


