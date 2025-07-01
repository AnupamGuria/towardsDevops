2. Student Grades

#dictionay grade
grade={"Ajay":"A","Bhumi":"C","Deepak":"D","Joy":"A","Manoj":"F","Nitish":"B"}

#adding new student
new_name, new_grade=input("Enter new student name and grade: ").split()
grade[new_name]=new_grade

#update existing student's grade
updated_name, updated_grade = input("Enter the existing name and updated grade: ").split()
if updated_name in grade.keys(): grade[updated_name]=updated_grade
else: print(f"{updated_name} Student does not exist")

#print all students grade using for loop
print("Student's grades as follows:")
for k,v in grade.items():
    print(f"{k}: {v}")

3.


4. Read from a File
file = open("python.txt","r")
content=file.read()
file.close()
print(content)
