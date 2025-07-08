class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):  # This defines how to convert to string
        return f"Person named {self.name}"

person = Person("Alice")
print(person)  # Automatically calls str(person)
# Output: Person named Alice