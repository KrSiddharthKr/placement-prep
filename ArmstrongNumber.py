def checkArmstrongNumber(n):
    originalNumber = n
    digits = []
    while n>0:
        digits.append(n%10)
        n = n//10
    numOfDigits = len(digits)
    armstrongNumberSum = sum(d ** numOfDigits for d in digits)
    if armstrongNumberSum == originalNumber:
        return True
    else:
        return False

number = int(input())
print(checkArmstrongNumber(number))