string = str(input())
lower = string.lower()
length = len(string)
x = 0

while x < length:
    temp = lower[x]
    n = 1
    i = x + 1

    while i < length and lower[i] == temp:
        n += 1
        i += 1

    print(temp + str(n), end="")

    x = i
