number = int(input("Enter the number: "))
sum = 0
while number>0:
    digit = number%10
    sum = sum + (digit*digit)
    number //= 10
print(sum)