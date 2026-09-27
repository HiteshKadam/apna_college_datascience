# #FILE IO

# f = open("sample.txt","w") #file object
# # print(f.read())
# f.write("dwhduwd \n dawdawdaw")

# # print(f.readline())
# f.close()

# # Modes
# '''
# r = read
# w = write
# x = create and write
# a = append
# b = binary mode
# t = text mode
# + = update (r & w)
# '''

# with open("sample.txt","r") as f:
#     print(f.read())


# # delete file using os module

# import os

# os.remove("sample.txt")


# #Exception handling
# # try except else finally

# try:
#     x = int(input("enter x: "))
#     y = 10/x
# except ZeroDivisionError:
#     print("Captured zero division error")
# except ValueError:
#     print("Invalid input")
# else:
#     print(y)
# finally:
#     print("Code now done!")

# #List comprehension
# # [output for loop  condition]
# list1 = [i*i for i in range(6)]
# print(list1)

#json
import json

with open("data.json","r") as f:
    py_obj = json.load(f)
    print(py_obj)