A = int(input())
B = int(input())
C = int(input())
print(1 <= A <= 180)
print(1 <= B <= 180)
print(1 <= C <= 180)
if (1 <= A <= 180) and (1 <= B <= 180) and (1 <= C <= 180):
    if (A+B+C)==180:
        print(1)
    else:
        print(0)