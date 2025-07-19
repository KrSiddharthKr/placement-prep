def isPrime(n):
    factors = 0
    for x in range(1, int(n**0.5)+1):
        y = n/x
        if n%x==0:
            if x==y:
                factors += 1
            else:
                factors += 2
    if factors == 2:
        return True
    else:
        return False
    
number = int(input())     
print(isPrime(number))