print("Hello \n World") 

name ="Hitesh"
age = 26
PI = 3.14

print("My name is : ",name)

print(type(age)) #thi sis single line comment

'''
This is
multi line comment
'''

# style guide

dot_price = 100 #snake case  * preffered
dotPrice = 100 # camelcase
DotPrice = 100 #Pascal Case

# Operations

a = 5
b =10

# Arithmetic operators
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b % a)
print(a ** b)
print(a // b)

# Relational Operators

print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)


# Assignment
a = 5
a += 1
a -= 1
a *= 10
a /= 10

#Logical operator

print(not True)
print(True and False)
print(True or False)


x = 3
x+=5
print(x)



#Operator Precedence. VBODMAS
'''
()
**
*,/,%
+,-
==, !=, >,>=,<,<=
not
and
or
'''

#Type Conversion
'''
Type Conversion (Implicit/Automatic)
Casting(Explicit)
'''


ans1 = int(5+10.0)
ans2 = 5 + 10.0

print(ans1, type(ans1))
print(ans2, type(ans2))


#Input

# a = input("Enter value of a")
# print(a)

#Avg
a = float(input("First number: ")) 
b = float(input("Second number: ")) 

avg = (a + b)/2
print(avg)