# print even numbers from 1 to N
# number = int(input("Enter the number: "))
# i = 1
# while i<=number:
#     if(i%2==0):
#         print(i)
#         i += 1
#         continue
#     i += 1

# Print sum of Even numbers from 1 to N
number = int(input("Enter the number: "))
i = 1
sum = 0
while i<=number:
    if(i%2==0):
        sum += i
        i += 1
        print(sum)
        continue
    i += 1