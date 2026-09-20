#Q1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello",name,"you are",age,"years old!")


#Q2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)
print(a - b)
print(a * b)
print(a / b)

#Q3
x = int(input("Enter first int number: "))
y = int(input("Enter second int number: "))
z = float(input("Enter float number: "))

avg = (float(x) + float(y) + float(z))/3
print(avg)

#Q4
num = input("Enter your number: ")
num = float(num)
print(num, type(num))
num = int(num)
print(num, type(num))
num = str(num)
print(num, type(num))

#Q5
x = 10 + 3 * 2 ** 2
print(x)

#Q6
x = int(input("Enter first int number: "))
y = int(input("Enter second int number: "))
print(x , y)

x, y = y, x

print(x , y)


#Q7
temperature = float(input("Enter Temperature in celsius: "))
farenheit_temp = (temperature * (9/5)) + 32
print(farenheit_temp)

#Q8
r = int(input("Enter radius int number: "))
PI = 3.14
area = PI * r ** 2
print(area)

#Q9
P = float(input("Enter principal int number: "))
R = float(input("Enter rate int number: "))
T = float(input("Enter time int number: "))

SI = (P * R * T )/100
print(SI)

#Q10
x = float(input("Enter float number: "))
print(int(x))
print(x % int(x))