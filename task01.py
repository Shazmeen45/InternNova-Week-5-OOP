class Student:
    def display_info(self):
        print("Student name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

#creating object
student1 = Student()
student1.name = "Shazmeen"
student1.age = 22
student1.course = "Artificial Intelligence"

student2 = Student()
student2.name = "Zaid"
student2.age = 23
student2.course = "Cyber Security"

# Displaying student information
student1.display_info()
print()
student2.display_info()
