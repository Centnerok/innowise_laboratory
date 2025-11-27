def print_menu():
    '''
    This function display the menu
    '''
    print("---------")
    print("1.   Add a new student")
    print("2.   Add grades for a student")
    print("3.   Generate a full report")
    print("4.   Find the top student")
    print("5.   Exit program")

def add_new_student(students):
    '''
    This function adding new student to the list students
    '''
    name = input("Please, enter a new student name:    ").upper()

    for student in students:
        if student["name"] == name:
            return 0
        
    return {
        "name":name,
        "grades":[]
    }

def add_student_grade(students):
    '''
    This function adding grades to chosen students record
    '''
    name = input("Please, enter a students name:    ").upper()

    student_found = False

    for student in students:
        if student["name"] == name:
            student_found = True
            grade = 0
            while grade != "done":
                grade = input("Enter a grade(or 'done' to finish):  ").lower()
                if grade != "done":
                    try:
                        student["grades"].append(int(grade))
                    except ValueError:
                        print("ERROR! Invalid value!")
    if not student_found:
        print("This student doesnt exist!")

def show_report(students):
    '''
    This function calculate and displays average grade for each student, maximum, minimum and overall grade
    '''
    average_grades = []
    if not students:
        print("There are no students!")
        return
        
    for student in students:
        average_grade = 0
        grades_len = len(student["grades"])
        for i in student["grades"]:
            average_grade += i
        try:
            average_grade = average_grade / grades_len
        except ZeroDivisionError:
            average_grades.append("N/A")
        else:
            average_grades.append(average_grade)

    max_avg = 0
    min_avg = 100
    overall_avg = 0

    for avg in average_grades:
        if isinstance(avg, (int, float)):
            max_avg = avg
            min_avg = avg
            break

    for i in range(len(average_grades)):
        print(f"{students[i]['name']}'s average grade is {average_grades[i]:.1f}.")
        if isinstance(average_grades[i], (int, float)):
            if average_grades[i] > max_avg:
                max_avg = average_grades[i]
            if average_grades[i] < min_avg:
                min_avg = average_grades[i]

    valid_grades = [avg for avg in average_grades if isinstance(avg, (int, float))]

    if valid_grades:
        overall_avg = sum(valid_grades) / len(valid_grades)
    else:
        overall_avg = "N/A"

    print("Max Average:     ", f"{max_avg:.1f}")
    print("Min Average:     ", f"{min_avg:.1f}")
    print("Overall Average:     ", f"{overall_avg:.1f}")
        

def find_top_performer(students):
    '''
    This function finding the top performer
    '''
    valid_students = []
    for student in students:
        if "grades" in student and student["grades"] and len(student["grades"]) > 0:
            average_grade = sum(student["grades"]) / len(student["grades"])
            valid_students.append((student, average_grade))

    top_student = max(valid_students, key=lambda x: x[1])
    
    print(f"Top performer: {top_student[0]['name']} with average grade {top_student[1]:.1f}")

    if not students:
        print("No students added!")
        return
    
    students_with_grades = [s for s in students if "grades" in s and s["grades"] and len(s["grades"]) > 0]
    
    if not students_with_grades:
        print("No students with valid grades found!")
        return
    
    top_student = max(students_with_grades, 
                     key=lambda student: sum(student["grades"]) / len(student["grades"]))
    
    avg_grade = sum(top_student["grades"]) / len(top_student["grades"])
    
    print(f"Top performer: {top_student['name']} with average grade {avg_grade:.1f}")