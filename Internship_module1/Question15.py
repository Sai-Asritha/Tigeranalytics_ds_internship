def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result
def binomial_coefficient(n, r):
    return factorial(n)//(factorial(r)*factorial(n - r))
n = int(input())
m = int(input())
ways = binomial_coefficient(n - m + 1, m)
print(ways)
