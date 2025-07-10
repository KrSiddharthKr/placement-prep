number = int(input("Enter the number: "))
i = 1
sum = 0
while number>0:
    # print("Entered the loop")
    if (i%2==0):
        sum += i
        # print("sum is: ", sum)
        i += 1
        # print("i inside of if-block: ", i)
        number -= 1
        # print("number is: ", number)
        continue
    i += 1
    # print("i outside of if-block: ", i)
print(sum)