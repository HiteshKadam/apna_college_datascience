# Conditional Statement
# if, elif, else

color = input("Enter your color: ")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Look")
elif color == "green":
    print("Go")
else:
    print("Invalid color")


age = int(input("Enter your age: "))
if age < 13 :
    print("Child")
elif age >= 13 and age < 18 :
    print("Teenager")
elif age >= 18:
    print("Adult")
else:
    print("Invalid input")


# Match
val = input("Enter your color: ")
match val:
    case "red": print("Stop")
    case "yellow": print("Look")
    case "green": print("Go")
    case _: print("wrong color")

# Loops
# Infinite Loop
while True:
    print("Hello World")

# Controlled Loop

count = 1
while count <= 5:
    print("Hello World")
    count += 1

count = 5
while count >= 1:
    print("Hello World",count)
    count -= 1

num = int(input("Enter your number: "))
i = 1
while i <= 10:
    print(num,"x",i,"=",num * i)
    i += 1

#For Loop
for i in "Hello":
    print(i)

if "o" in "Hello":
    print("Present")


for i in range(5):
    print(i)

word = "artificial intelligence"
count = 0
for i in word:
    if i == 'i':
        count += 1
print(count)

n = int(input("Enter your number: "))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)

