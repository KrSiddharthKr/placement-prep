A = 393491
number = 0
while A>0:
    digit = A%10
    print(digit)
    number = number*10 + digit
    print(number)
    A = A//10
    print(A)