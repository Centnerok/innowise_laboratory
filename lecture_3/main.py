import functions as fun

students = []

while True:
    fun.print_menu()

    try:
        answer = int(input("Enter your choice(integer):   "))
    except Exception as e:
        print("Error! ", e)
    else:
        if answer == 1:
            new_student = fun.add_new_student(students)
            if new_student == 0:
                print("This student already exist!")
            else:
                students.append(new_student)

        elif answer == 2:
            fun.add_student_grade(students)

        elif answer == 3:
            fun.show_report(students)

        elif answer == 4:
            fun.find_top_performer(students)

        elif answer == 5:
            break