def student(students):
    for I in range(len(students)):
        students[i] = input("Enter student ID: ").strip(), input("Enter student name: ").strip(), input("Enter student DOB (YYYY-MM-DD): ").strip()

def course(courses):
    for I in range(len(courses)):
        courses[i] = input("Enter course ID: ").strip(), input("Enter course name: ").strip()

def select_course(students, courses):
    print("Courses:")
    for course in courses:
        print(course[0], "-", course[1])
    course_id = input("Enter course ID: ")
    for i, (student_id, student_name, _) in enumerate(students):
        if (course_id,) in [(course[0t],) for course in courses if student_id in [student[0] for student, _ in students]]:
            marks = []
            while True:
                mark = input("Enter mark (or 'done' to finish): ")
                if mark == 'done':
                    marks.append('done')
                    break
                try:
                    marks.append(float(mark))
                except ValueError:
                    print("Invalid mark. Please enter a number.")
            students[i] = (student_id, student_name, marks)
            print("Marks updated for", student_name)
            return students, courses
    print("Student not found.") return students, courses

def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(course[0], "-", course[1])
    
def list_students(students):
    print("Students:")
    for student in students:
        id, name, marks = student  
        Print(f"{id} - {name}") if len(marks) == len(['done' for _ in marks]) else print(f"{id} - {name} ({', '.join([str(mark) for mark in marks])})") 