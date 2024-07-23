class Student:
    def __init__(self, email, names):
        """Initialize a new student with email and names."""
        self.email = email
        self.names = names
        self.courses_registered = {}
        self.GPA = 0.0

    def calculate_GPA(self):
        """Calculate and update the GPA based on registered courses.
        GPA is computed as the weighted average of grades."""
        total_credits = 0
        total_points = 0
        for grade, credits in self.courses_registered.values():
            total_credits += credits
            total_points += grade * credits

        self.GPA = total_points / total_credits if total_credits else 0

    def register_for_course(self, course_name, grade, credits):
        """Register the student for a course and update GPA."""
        self.courses_registered[course_name] = (grade, credits)
        self.calculate_GPA()


class Course:
    def __init__(self, name, trimester, credits):
        """Initialize a new course with name, trimester, and credits"""
        self.name = name
        self.trimester = trimester
        self.credits = credits


class GradeBook:
    def __init__(self):
        """Initialize the grade book with empty student and course lists."""
        self.students = []
        self.courses = {}

    def add_student(self, email, names):
        """Add a new student to the grade book. Check for existing email to avoid duplicates."""
        if any(student.email == email for student in self.students):
            print("Error: Student with this email already exists.")
        else:
            self.students.append(Student(email, names))
            print("Student added successfully.")


    def add_course(self, name, trimester, credits):
        """dd a new course to the grade book. Ensure the course does not already exist."""
        if name in self.courses:
            print("Error: Course already exists.")
        else:
            self.courses[name] = Course(name, trimester, credits)
            print("Course added successfully.")

    def register_student_for_course(self, email, course_name, grade):
        """Register a student for a course by updating their records.Handle errors for non-existing students or courses. """
        student = next((s for s in self.students if s.email == email), None)
        course = self.courses.get(course_name)

        if student is None:
            print("Error: Student does not exist.")
        elif course is None:
            print("Error: Course does not exist.")
        else:
            student.register_for_course(course_name, grade, course.credits)
            print(f"Student {email} registered for course {course_name}.")

    def calculate_ranking(self):
        """Return a sorted list of students based on their GPA."""
        return sorted(self.students, key=lambda s: s.GPA, reverse=True)

    def search_by_grade(self, course_name, min_grade, max_grade):
        """Find students who have a grade within the specified range for a course."""
        return [s for s in self.students if course_name in s.courses_registered and
                min_grade <= s.courses_registered[course_name][0] <= max_grade]

    def generate_transcript(self, email):
        """Generate a transcript for a student with their GPA and course details."""
        student = next((s for s in self.students if s.email == email), None)
        if student:
            return {
                "email": student.email,
                "names": student.names,
                "GPA": student.GPA,
                "courses": student.courses_registered
            }
        else:
            print("Error: Student not found.")
            return None

    def display_courses(self, email):
        """Display all courses a student is registered for."""
        student = next((s for s in self.students if s.email == email), None)
        if student:
            print(f"Courses for {student.names}:")
            for course, (grade, credits) in student.courses_registered.items():
                print(f"Course: {course}, Grade: {grade}, Credits: {credits}")
        else:
            print("Error: Student not found.")

    def list_all_students(self):
        """List all students and the courses they are registered for."""
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            print(f"Student: {student.names} (Email: {student.email})")
            if student.courses_registered:
                print("Courses:")
                for course, (grade, credits) in student.courses_registered.items():
                    print(f"  Course: {course}, Grade: {grade}, Credits: {credits}")
            else:
                print("  No courses registered.")


def main():
    """Main function to interact with the grade book application."""
    grade_book = GradeBook()

    while True:
        print("\nSelect an option:")
        print("1.Add Student")
        print("2.Add Course")
        print("3.Register Student for Course")
        print("4.Calculate GPA for All Students")
        print("5.Calculate Ranking")
        print("6.Search by Grade")
        print("7.Generate Transcript")
        print("8.Display Courses for Student")
        print("9.List All Students")
        print("10.Exit")

        choice = input("Choose an action: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            grade_book.add_student(email, names)

        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter credits: "))
            grade_book.add_course(name, trimester, credits)

        elif choice == '3':
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            grade_book.register_student_for_course(email, course_name, grade)

        elif choice == '4':
            print("GPA calculation is not yet implemented for all students.")

        elif choice == '5':
            ranking = grade_book.calculate_ranking()
            print("Student Rankings:")
            for student in ranking:
                print(f"Student: {student.names}, GPA: {student.GPA:.2f}")

        elif choice == '6':
            course_name = input("Enter course name: ")
            min_grade = float(input("Enter minimum grade: "))
            max_grade = float(input("Enter maximum grade: "))
            results = grade_book.search_by_grade(course_name, min_grade, max_grade)
            if results:
                print("Students found:")
                for student in results:
                    print(f"Student: {student.names}, Grade: {student.courses_registered[course_name][0]}")
            else:
                print("No students found with the specified grade range.")

        elif choice == '7':
            email = input("Enter student email: ")
            transcript = grade_book.generate_transcript(email)
            if transcript:
                print(f"Transcript for {email}:")
                print(f"Names: {transcript['names']}")
                print(f"GPA: {transcript['GPA']:.2f}")
                for course, (grade, credits) in transcript['courses'].items():
                    print(f"Course: {course}, Grade: {grade}, Credits: {credits}")

        elif choice == '8':
            email = input("Enter student email: ")
            grade_book.display_courses(email)

        elif choice == '9':
            grade_book.list_all_students()

        elif choice == '10':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
