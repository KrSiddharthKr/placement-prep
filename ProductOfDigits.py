def productOfDigits(n):
    if n == 0:
        return 0
    if n<0:
        n = abs(n)
    prod = 1
    while n>0:
        digits = n%10
        prod *= digits
        n = n//10
    return prod

number = int(input())
print(productOfDigits(number))