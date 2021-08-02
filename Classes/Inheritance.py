from CreateObject import Person

class Student (Person):
    def __init__(self, name, age, class_name):
        super().__init__(name, age)
        self.class_name = class_name

new_student = Student("Ana", 18, "12A1")
new_student.myfunc()
print(new_student.class_name)