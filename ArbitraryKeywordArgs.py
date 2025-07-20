# **kwargs
# def info_person(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key,value in kwargs.items():
#         print(key, value)

# info_person(name="Ram", age=30, dept="CSE")
# info_person(name="Shyam", dept="CSE")

def multiple_info(*args, **kwargs):
    print(kwargs)
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key, value)
    print(args)
    print(type(args))
    sum = 0
    for i in args:
        sum += i
    print(sum)

multiple_info(1,2,3,4,5,6,name="Ram", age=30, dept="CSE")
multiple_info(2,44,5,77, name="Shyam", dept="CSE")