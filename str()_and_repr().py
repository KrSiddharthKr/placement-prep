# text = "Hello World"
# number = 42
# none_value = None

# print("Using str(): ")
# print(str(text))
# print(str(number))
# print(str(none_value))

# print("\nUsing repr(): ")
# print(repr(text))
# print(repr(number))
# print(repr(none_value))

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    def __str__(self):
        return f"User(username={self.username!r}, email={self.email!r})"
    
user1 = User("alice", "alice@gmail.com")
user2 = User("alice ", "alice@gmail.com")

print(f"User 1: {user1.username!r}")
print(f"User 2: {user2.username!r}")

print(user1)
print(user2)