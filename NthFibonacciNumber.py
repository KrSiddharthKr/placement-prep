def nthFibonacciNumber(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    prev = 0
    curr = 1
    for _ in range(3, n+1):
        next = prev + curr
        prev = curr
        curr = next
    
    return curr

number = int(input())
print(nthFibonacciNumber(number))