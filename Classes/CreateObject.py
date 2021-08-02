class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36)
p2 = Person("Smith", 25)

print(p1.name)
print(p1.age)
print(Person.count)
print(p1.count)

p1.name = 'Peter'
p1.myfunc()