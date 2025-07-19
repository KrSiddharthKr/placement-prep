def reversedNumber(n):
    if n<0:
        n = abs(n)
    reversed = 0
    while n>0:
        digit = n%10
        reversed = reversed*10+digit
        n = n//10
    return reversed

number = int(input())
print(reversedNumber(number))