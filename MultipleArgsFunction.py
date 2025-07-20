def add(*numbers):
    print(type(numbers))
    print(numbers)
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8,9,10))