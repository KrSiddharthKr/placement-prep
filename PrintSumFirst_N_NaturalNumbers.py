# sum of first N natural numbers
# number = int(input("Enter the number: "))
# sum = 0
# i = 1
# while i<=number:
#     sum += i
#     i += 1
# print(sum)

# sum of square of first N natural numbers
# number = int(input("Enter the number: "))
# sum = 0
# i = 1
# while i<=number:
#     sum += (i*i)
#     print(sum)
#     i += 1
# print(sum)

# sum of first N natural numbers
number = int(input("Enter the number: "))
sum = 0
i = 1
while i<=number:
    sum += ((i*i)*i)
    print(sum)
    i += 1
print(sum)