class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_course(self):
        print("Course:", self.course)


# Creating student objects
student1 = Student("Shazmeen", 22, "Artificial Intelligence")
student2 = Student("Zaid", 23, "Cyber Security")

# Displaying information
student1.display_info()
student1.display_course()
print()
student2.display_info()
student2.display_course()
