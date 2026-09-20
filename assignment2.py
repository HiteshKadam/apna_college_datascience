#Q1
salary = int(input("Enter your salary: "))
if salary < 30000:
    print(salary * 5 / 100)
elif salary >= 30000 and salary <= 70000:
    print(salary * 15 / 100)
elif salary > 70000:
    print(salary * 25 / 100)

#Q2
a = int(input("Enter number first: "))
b = int(input("Enter number second: "))
for i in range (a,b+1):
    if i % 2 == 0:
        print(i)

#Q3
num = int(input("Enter number: "))
while num != 0:
    digit = num % 10
    print(digit)
    num = int(num / 10)

#Q4
num = int(input("Enter number: "))
count = 0
while num != 0:
    digit = num % 10
    count +=1
    num = int(num / 10)
print(count)

#Q5
num = int(input("Enter number: "))
sum = 0
while num != 0:
    digit = num % 10
    sum +=digit
    num = int(num / 10)
print(sum)

#Q6
for i in range(1,101):
    if(i % 3 == 0 and i % 5 == 0):
        print(i)

#Q7
action = "input"
while action != "Quit":
    n = int(input("Enter number: "))
    if n > 0:
        print("Positive")
    else:
        print("Negative")
    action = input("Type Quit to exit: ")

#Q8
def calculator(a, b, ops):
    if ops == '+':
        return a + b
    if ops == '-':
            return a - b
    if ops == '*':
            return a * b
    if ops == '/':
            return a / b
print(calculator(2,3,'*'))

#Q9
def is_prime(n):
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True

print(is_prime(2))   

#Q10
magic = 109
guess = int(input("Guess number: "))
while True:
    if guess > magic:
        print("Too high")
    elif guess < magic:
        print("Too low")
    else:
        print("Correct!")
        break
    guess = int(input("Guess number: "))