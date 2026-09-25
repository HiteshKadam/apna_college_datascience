#OOPS
class Student:
    subject = "Python"

    def __init__(self,name):
        self.name = name
        print("Constructor was called")

stu1 = Student("Rahul")
print(stu1.name)