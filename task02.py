class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print("Student name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

# Creating objects with different values
student1 = Student("Shazmeen", 22, "Artificial Intelligence")
student2 = Student("Zaid", 23, "Cyber Security")

# Accessing initialized attributes
print("Student1 course:", student1.course)
print("Student2 course:", student2.course)
print()

# Displaying complete information
student1.display_info()
print()
student2.display_info()

