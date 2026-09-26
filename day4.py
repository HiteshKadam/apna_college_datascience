#OOPS
class Student:
    college = "ABC College" # class attributes

    #self is like this pointing to object
    #multiple constructor is not allowed
    def __init__(self,name,cgpa): # parameterized constructor
        self.name = name  #Instance attributes
        self.cgpa = cgpa

    def get_cgpa(self):  # Methods
        return self.cgpa



stu1 = Student("Rahul",9.0)
print(stu1.name)
print(stu1.get_cgpa())
print(stu1.college)


#class & instance
#attributes: class and instance
#methods: class,instance and static


class Laptop:
    storage_type = "ssd"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self): #instance method
        print(self.RAM,self.storage,self.storage_type)

    @classmethod #decorator
    def get_storage_type(cls): #class method
        print(cls.storage_type)

    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (price*discount/100)
        print(final_price)

l1 = Laptop("512GB","1TB")
l1.get_info()
l1.get_storage_type()
l1.calc_discount(40_000,10)