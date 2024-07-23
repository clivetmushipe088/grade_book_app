from grade_book import Student, Course, GradeBook

def main():
    grade_book = GradeBook()

    while True:
        print("\nPick a number from 1 to 8 to select an action as shown bellow")
        print("1. Add a student")
        print("2. Add a course")
        print("3. Register student for course")
        print("4. Calculate GPA")
        print("5. Calculate ranking")
        print("6. Search by grade")
        print("7. Generate transcript")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            email = input("Enter student email (e.g clivetmushipe@gmail.com): ")
            names = input("Enter student names: ")
            grade_book.add_student(Student(email, names))
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter credits: "))
            grade_book.add_course(Course(name, trimester, credits))
        elif choice == '3':
            email = input("Enter existing students email: ")
            course_name = input("Enter existing course name: ")
            grade = float(input("Enter grade: "))
            grade_book.register_student_for_course(email, course_name, grade)
        elif choice == '4':
            grade_book.calculate_GPA()
            print("GPA calculated for all students.")
        elif choice == '5':
            ranking = grade_book.calculate_ranking()
            for rank, student in enumerate(ranking, 1):
                print(f"Rank {rank}: {student.names} - GPA: {student.GPA}")
        elif choice == '6':
            course_name = input("Enter course name: ")
            grade_range = input("Enter grade range (e.g., 80-90): ").split('-')
            grade_range = range(int(grade_range[0]), int(grade_range[1]) + 1)
            students = grade_book.search_by_grade(course_name, grade_range)
            for student in students:
                print(f"{student.names} - {course_name}: {student.courses_registered[course_name]}")
        elif choice == '7':
            email = input("Enter student email: ")
            transcript = grade_book.generate_transcript(email)
            print(transcript)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
