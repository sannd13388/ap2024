import datetime
noStudent = int(input("Enter number of students: "))

i=0
while i<noStudent :
    studentID = int(input("Enter student ID: "))
    studentName = str(input("Enter student name: "))
    studentDoB = input("enter DoB: ")
    studentList = {"studentID": studentID,
               "studentName": studentName,
               "studentDoB": studentDoB}
    i+=1
    

noCourse = int(input("Enter number of course: "))
while i<noCourse:
    courseID = int(input("Enter course ID: "))
    courseName = str(input("Enter name of the course: "))
    courseList = {"courseID": courseID, 
                  "courseName": courseName}
    i+=1

courseMark = float(input("Enter mark: "))
courseList.update({"Mark": courseMark})

list = {"studentList": studentList,
        "courseList": courseList}

print(list)