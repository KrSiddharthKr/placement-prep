'''
Given an integer n. Write a program to return the last digit of the number.

Examples:

Input: n = 10
Output: 0
Input: n = 9768
Output: 8
Constraints:

-10^9 ≤ n ≤ 10^9

Expected Complexities
Time Complexity: O(1)
Auxiliary Space: O(1)


Solution:
what should be the answer of a -ve number % positive number?

Edit
Great question! The behavior of negative number % positive number depends on the programming language, but let me explain Python's specific behavior:

Python's Behavior
In Python, the result of a % b always has the same sign as the divisor (b).

python
print(-7 % 3)   # Output: 2
print(-5 % 2)   # Output: 1
print(-10 % 4)  # Output: 2
Why does -7 % 3 = 2?
Step-by-step calculation:

-7 ÷ 3 = -2.333...
Floor division: -7 // 3 = -3 (rounds down to nearest integer)
Remainder: -7 - (3 × -3) = -7 - (-9) = -7 + 9 = 2
Python's formula: a % b = a - (a // b) * b

Examples:
python
def show_modulo(a, b):
    quotient = a // b
    remainder = a % b
    print(f"{a} ÷ {b} = {quotient} remainder {remainder}")
    print(f"Verification: {quotient} × {b} + {remainder} = {quotient * b + remainder}")
    print()

show_modulo(-7, 3)
show_modulo(-5, 2) 
show_modulo(-10, 4)
show_modulo(-1, 5)
Output:

-7 ÷ 3 = -3 remainder 2
Verification: -3 × 3 + 2 = -7

-5 ÷ 2 = -3 remainder 1
Verification: -3 × 2 + 1 = -5

-10 ÷ 4 = -3 remainder 2
Verification: -3 × 4 + 2 = -10

-1 ÷ 5 = -1 remainder 4
Verification: -1 × 5 + 4 = -1
Key Rules in Python:
Result is always non-negative when divisor is positive
Range: 0 ≤ (a % b) < b when b > 0
Sign follows divisor: result has same sign as b
Different in Other Languages:
C/C++/Java: -7 % 3 = -1 (result follows dividend sign)
Python/Ruby: -7 % 3 = 2 (result follows divisor sign)
In Python: negative % positive always gives a positive result between 0 and (divisor-1).
abs(n) % 10
why is this correct?

Edit
Great question! Let me explain why abs(n) % 10 is correct step by step.

Understanding the Problem
The problem asks for the last digit of a number. The "last digit" means the digit in the ones place, regardless of whether the number is positive or negative.

What Does "Last Digit" Mean?
For any number, the last digit is the rightmost digit:

123 → last digit is 3
-123 → last digit is still 3 (we ignore the negative sign)
9768 → last digit is 8
-9768 → last digit is still 8
Why abs(n) % 10 Works
Step 1: abs(n) removes the sign

python
abs(123) = 123
abs(-123) = 123    # Sign is removed
abs(-7) = 7
abs(10) = 10
Step 2: % 10 gets the last digit

python
123 % 10 = 3      # Last digit of 123
7 % 10 = 7        # Last digit of 7  
10 % 10 = 0       # Last digit of 10
9768 % 10 = 8     # Last digit of 9768
Why This Logic Makes Sense
The mathematical meaning of "last digit":

Any number can be written as: number = (some_multiple_of_10) + last_digit
Examples:
123 = 120 + 3
9768 = 9760 + 8
10 = 10 + 0
The modulo operation n % 10 gives us exactly this last digit part.

Visual Example
python
def demonstrate_last_digit(n):
    print(f"Number: {n}")
    print(f"Absolute value: {abs(n)}")
    print(f"Last digit: {abs(n) % 10}")
    print(f"Verification: {abs(n)} = {(abs(n) // 10) * 10} + {abs(n) % 10}")
    print("-" * 30)

# Test cases
for num in [123, -123, 9768, -10, 7, -7]:
    demonstrate_last_digit(num)
Output:

Number: 123
Absolute value: 123
Last digit: 3
Verification: 123 = 120 + 3
------------------------------
Number: -123
Absolute value: 123
Last digit: 3
Verification: 123 = 120 + 3
------------------------------
Why Not Just n % 10?
As we saw earlier, Python's modulo with negative numbers behaves differently:

python
print(-123 % 10)  # Output: 7 (not 3!)
This happens because Python ensures the result has the same sign as the divisor, which gives us the wrong answer for this problem.

The Key Insight
The sign doesn't matter for finding the last digit - we only care about the magnitude of the number. That's why abs(n) followed by % 10 gives us exactly what we need.

It's like asking "What's the last digit you see when you write this number?" - whether it's 123 or -123, you see the same digit 3 at the end.
'''
dividend = int(input())
divisor = 10
answer = abs(dividend) % 10
# if dividend<0:
#     answer = 0
# else:
#     answer = dividend%divisor
print(answer)