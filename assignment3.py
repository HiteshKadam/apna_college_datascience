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