'''
Given an input num as a string. You need to typecast into an integer and double it. 

Examples:

Input: num = "5"
Output: 10
Explanation: Typecast "5" to int and then double it 5 * 2 = 10
Input: num = "12"
Output: 24
Explanation: Typecast "12" to int and then double it 12 * 2 = 24
'''

num = input()
integer_value = int(num)
ans = integer_value * 2
print(ans)