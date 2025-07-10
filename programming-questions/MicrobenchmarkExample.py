import timeit

print(timeit.timeit("x = 123; x = int(x / 10)",number=1000000))
print(timeit.timeit("x = 123; x = x // 10",number=1000000))