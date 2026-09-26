# #Problem1

# class Product:
#     count = 0
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#         Product.count+=1

#     def get_info(self):
#         print(self.name,self.price)

#     @classmethod
#     def get_count(cls):
#         print(cls.count)

#     @staticmethod
#     def calc_discount(price,discount):
#         final_price = price - (discount*price/100)
#         print(final_price)


# p1 = Product("Mobile",200)
# p2 = Product("Laptop",600)
# p3 = Product("CPU",450)
# p1.calc_discount(p1.price,20)
# p1.get_info()
# p1.get_count()

# #Q1
# class BankAccount:
#     def __init__(self, account_number, owner_name, balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance

#     def deposit(self, deposit):
#         self.balance += deposit

#     def withdraw(self,withdraw):
#         self.balance -= withdraw

#     def check_balance(self):
#         print(self.owner_name,self.balance)

# b1 = BankAccount("234343414","Hitesh",30000)
# b1.check_balance()
# b1.deposit(10000)
# b1.check_balance()
# b1.withdraw(5000)
# b1.check_balance()

#Q2
# class Book:
#     def __init__(self, title, author, reviews):
#         self.title = title
#         self.author = author
#         self.reviews = [reviews]

#     def add_review(self,review):
#        self.reviews.append(review)

#     def count_review(self):
#         print(len(self.reviews))

#     def display_review(self):
#         print(self.reviews)

# b1 = Book("Abc","Hitesh","Good")
# b1.add_review("Bad")
# b1.display_review()
# b1.count_review()

# #Q3
# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.__name = name
#         self.__roll_no = roll_no
#         self.__marks= marks

#     def set_marks(self,marks):
#         if marks >= 0:
#             self.__marks = marks

#     def set_roll_no(self,roll_no):
#             if roll_no > 0 and roll_no <= 100:
#                 self.__roll_no = roll_no

#     def set_name(self,name):
#             if name != None or name != "":
#                 self.__name = name

# #Q4

# class Shape():
#     def area():
#         pass

# class Circle(Shape):
#     def area():
#         print("pi*r^2")

# class Rectangle(Shape):
#     def area():
#         print("Side ^ 2")

# class Triangle(Shape):
#     def area():
#         print("0.5 * base * height")

#Q10
class Message:
    message_counter=1 # simple counter
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter = 1

    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"

class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None
        def send_message(self, content):
            if not self.chatroom:
                print(f"{self.username} cannot send a message (not in a chatroom).")
            else:
                self.chatroom.broadcast(self, content)

class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def remove_user(self, user):
        self.users.remove(user)
    
    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message) # Show message to all users
    
    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages:
            print(msg)
        print()