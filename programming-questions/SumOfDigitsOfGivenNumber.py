number = int(input("Enter the number: "))
sum = 0
while number>0:
    digit = number%10
    sum += digit
    number = number//10
    # print(number)
print(sum)