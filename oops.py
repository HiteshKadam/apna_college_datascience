# #Encapsulation
# '''
# python uses it only by convention 

# public - accessible everywhere
# protected - its still accessible using _variable_name (Data Hiding)
# private - it needs getters and setters but can also be accessed via object.class.variable (data Mangling)

# '''


# class BankAccount:

#     def __init__(self, name, balance):
#         self.name = name # public
#         # self._balance = balance #protected
#         self.__balance = balance # private

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self, balance):
#         self.__balance = balance



# b1 = BankAccount("Hitesh",20000)
# print(b1.name,b1.get_balance())
# print(b1.name,b1._BankAccount__balance)

# Inheritance

# class Employee:
#     start_time = "10am"
#     end_time = "6pm"

#     def change_time(self, new_time):
#         self.end_time = new_time


# class Teacher(Employee): #Single Inheritance
#     def __init__(self, subject):
#         self.subject = subject

# class Accountant(Teacher): #MultiLevel Inheritance
#     def __init__(self, role, subject):
#         super().__init__(subject)
#         self.role = role

# t1 = Teacher("Match")
# a1 = Accountant("Accountant","Maths")
# t1.change_time("5pm")
# print(t1.subject,t1.start_time,t1.end_time)
# print(a1.role,a1.start_time,a1.end_time,a1.subject)

# class Teacher:
#     def __init__(self, subject):
#         self.subject = subject

# class Student:
#     def __init__(self, classr):
#         self.classr = classr

# class TA(Teacher,Student): #Multiple Inheritance
#     def __init__(self, subject, classr, name):
#         super().__init__(subject)
#         Student.__init__(self,classr)
#         self.name = name

# t1 = TA("maths","1A","Hitesh")
# print(t1.name,t1.classr,t1.subject)

## Abstraction
# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def make_sound():
#         pass

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow")

# class Lion(Animal):
#     def make_sound(self):
#         print("Roar!")

#Polymorphism
# Function Overriding
# Duck typing