n=int(input("Enter a number: "))
temp=n
sum_of_powers=0
length=len(str(n))

while temp > 0:
    digit=temp % 10
    sum_of_powers+=digit ** length
    temp//=10

if sum_of_powers==n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
