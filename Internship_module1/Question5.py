letters=0
digits=0
word=str(input("enter the word"))
letter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit="0123456789"
for i in word:
    if i in letter:
        letters=letters+1
    elif i in digit:
        digits=digits+1
print("LETTERS ",letters)
print("DIGITS ",digits)
