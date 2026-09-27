# #p1

# def get_word(file,word):
#     line_num = 0
#     with open(f"{file}","r") as f:
#         for i in f.readlines():
#             if word in i :
#                 line_num +=1
#                 return line_num
#         return f"{word} not present"

# print(get_word("practice.txt","Python"))

# #Q1
# with open("names.txt","w") as f:
#     for i in range(5):
#         name = input("Enter the name:")
#         f.write(name + "\n")
# with open("names.txt","r") as f:
#     name = f.readline()
#     while name:
#         print(name)
#         name = f.readline()

# #Q2
# with open("logs.txt","a") as f:
#     f.write("Program run successfully\n")
# with open("logs.txt","r") as f:
#     log = f.readline()
#     while log:
#         print(log)
#         log = f.readline()

# #Q3
# num = [5, 10, 15, 20, 25]
# greater = [i for i in num if i > 15]
# print(greater)

# #Q4
# import json
# cities = {
#     "Mumbai":124123,
#     "Banglore":123414,
#     "Pune":231441
# }
# with open("cities.json","w") as f:
#     json.dump(cities,f, indent=4)

# new_city = input("Enter new city:")
# new_population = int(input("Enter new population:"))
# add_obj = {}
# with open("cities.json","r") as f:    
#     add_obj = json.load(f)

# with open("cities.json","w") as f:
#     add_obj[new_city] = new_population
#     json.dump(add_obj,f, indent=4)

# #Q5
# try:
#     with open("blablah.txt","r") as f:
#         print("file found")
# except FileNotFoundError:
#     print("File not found!")