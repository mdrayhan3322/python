
class Student:
    name =""
    age = 0
    cgpa = 0
class New_student(Student):
    pass
ans = New_student()
ans.name = "Rayhan"
ans.age = 20
ans.cgpa = 3.50
print(ans.name)
print(ans.age)
print(ans.cgpa)