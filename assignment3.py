#p1
info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English"),
]

subjects = set()
eng_students = set()
student_dict = {}
for sub in info:
    subjects.add(sub[1])
    if sub[1] == "English":
        eng_students.add(sub[0])

    if (student_dict.get(sub[0]) == None):
        student_dict.update({sub[0]:set()})
        student_dict[sub[0]].add(sub[1])
    else:
        student_dict[sub[0]].add(sub[1])


print(subjects)
print(eng_students)
print(student_dict)



#Q1
palindrome = input("Please enter your palindrome: ")

def check_palindrome(check):
    for i in range(0,len(palindrome)):
        if palindrome[i].lower() != palindrome[len(palindrome)-i-1].lower():
            return palindrome + " is not Palindrome"
    return palindrome + " is Palindrome"

print(check_palindrome(palindrome))

#Q2
avg_list = [1,2,34,4,6,7,57,10]
sum = 0
for i in avg_list:
    sum += i
print(sum / len(avg_list))

#Q3
list1 = [1, 2, 7]
list2 = [2, 4, 5]
result = list1+list2
result.sort()
print(result)

#Q4
tup1 = (1,2,3,4,5,6,7,8,9,10)
even = []
odd = []
for i in tup1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even_tup = tuple(even)
odd_tup = tuple(odd)
print(even_tup,odd_tup)

#Q5
students = {}
menu = input("Please enter A: Add Student, B: Update Marks, C: Search Student, D: Display all Students")
while menu != 'Q':
    match menu:
        case 'A':
            student = input("Enter Student Name: ")
            marks = int(input("Enter marks:"))
            if students.get(student):
                print("Student already present")
            else:
                students.update({student:marks})
        case 'B':
            student = input("Enter Student Name: ")
            marks = int(input("Enter marks:"))
            if students.get(student):
                students[student] = marks
            else:
                print("Student not Present")
        case 'C':
            student = input("Enter Student Name: ")
            if students.get(student):
                print(students[student])
            else:
                print("Student not Present")
        case 'D':
            print(students)
        case 'Q':
            break
    menu = input("Please enter A: Add Student, B: Update Marks, C: Search Student, D: Display all Students")


#Q6
words = ["apple", "banana", "kiwi", "cherry", "mango"]
fruits={}
for i in words:
    fruits.update({i:len(i)})
print(fruits)

#Q7
strin1 = input("Enter String with space: ")
count = 0
for i in strin1:
    if i == ' ':
        count+=1
print(count)

#Q8
list1 = [1, 2, 3, 4] 
list2 = [5, 6, 7, 8]

def check_common(lista,listb):
    set1 = set(lista)
    set2 = set(listb)

    result = set1.intersection(set2)
    if len(result) == 0:
        print("No Common Elements")
    else:
        print("Common Elements")

check_common(list1,list2)
list1 = [1, 2, 3]
list2 = [3, 4]
check_common(list1,list2)

#Q9
list3 = [1,2,2,2,3,4,5,6,6,6,7,7,8,8,9]
set3 = set(list3)
for i in set3:
    if list3.count(i) > 1:
        print(i,list3.count(i))

#Q10

str4 = input("Enter String")
set4 = set(str4)

print(set4)
for i in set4:
    print(i,str4.count(i))
