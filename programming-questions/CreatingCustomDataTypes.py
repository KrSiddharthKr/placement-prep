# Named Tuples
from collections import namedtuple

Person = namedtuple("Person", "name age")

person1 = Person("Bob", 30)
person2 = Person(name="Charlie", age=35)
print(person1.name)
print(person1.age)
print(person2)
print(person1)

print(person2.name)
print(person2.age)