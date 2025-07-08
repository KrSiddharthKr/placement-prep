'''
Given an integer N. FInd an integer K for which N%K is the largest ( 1 <= K < N).
Example 1:

Input:
N = 3
Output:
2
Explanation:
3%1 = 0
3%2 = 1
So, the modulo is highest for 2.
Example 2:

Input:
N = 4
Output:
3
Explanation:
4%1 = 0
4%2 = 0
4%3 = 1
So, the modulo is highest for 3.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^18
'''

# n = int(input("Enter n: "))
# k = int(input("Enter k: "))
# value = 0
# while k<n:
#     if((n%k!=0)):
#         if max(value, (n%k)):    
#             value=k
#             k += 1
#     else:
#         k += 1
# print(value)
a = 5
b = 1
while b<a:
    print(a%b)
    b+=1