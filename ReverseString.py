# string = "Siddhu"
# for i in range(0, len(string)//2):
#     start = string[i]
#     end = string[len(string) - i - 1]
#     string[len(string) - i - 1] = start
#     string[i] = end
    
# print(string)


'''
s = list("Kumar Siddharth")
left, right = 0, len(s)-1
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
print("".join(s))
'''

# string = list("hello")
# for i in range(0, len(string)//2):
#     start = string[i]
#     end = string[len(string) -  i - 1]
#     string[i] = end
#     string[len(string) -  i - 1] = start
# print("".join(string))


s = "Stringful"
print(s[-1::-1])