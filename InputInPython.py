'''
You need to perform three separate tasks based on the given input:

String Input and Print: Take a text input as a string and print it as it is.
Integer Input and Add: Take an integer input n, add 10 to it, and print the result.
Float Input and Multiply: Take a floating-point number as input, multiply it by 10, and print the result.
Examples:

Input: s = "Hello", n = 20, f = 5.5
Output: 
Hello
30
55.0
Explanation: 
The string Hello is printed as it is.
The integer 20 is increased by 10 and results in 30.
The floating-point number 5.5 is multiplied by 10 and results in 55.0
'''

s = input("enter s: ")
n = int(input("enter integer n: "))
f = float(input("enter floating number f: "))

print(s)

n += 10
print(n)

f *= 10
print(f)