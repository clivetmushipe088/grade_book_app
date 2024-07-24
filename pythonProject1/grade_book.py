#!/usr/bin/python3

class Student:
    def __init__(self, email, names):
        """
        Initialize a new student with email and names.
        """
        self.email = email
        self.names = names
        self.courses_registered = {}
        self.GPA = 0.0

    def percentage_to_gpa(self, percentage):
        """
        Convert a percentage grade to a GPA on a 1.0 to 4.0 scale.
        """
        if percentage >= 90:
            return 4.0
        elif percentage >= 80:
            return 3.0
        elif percentage >= 70:
            return 2.0
        elif percentage >= 60:
            return 1.0
        else:
            return 0.0

    def calculate_GPA(self):
        """
        Calculate and update the GPA based on registered courses.
        GPA is computed as the weighted average of grades.
        """
        total_credits = total_points = 0
        for grade, credits, max_score in self.courses_registered.values():
            normalized_grade = grade / max_score * 100  # Normalize grade to percentage
            gpa = self.percentage_to_gpa(normalized_grade)
            total_credits += credits
            total_points += gpa * credits

        self.GPA = total_points / total_credits if total_credits else 0

    def register_for_course(self, course_name, grade, credits, max_score):
        """
        Register the student for a course and update GPA.
        """
        self.courses_registered[course_name] = (grade, credits, max_score)
        self.calculate_GPA()

class Course:
    def __init__(self, name, trimester, credits, max_score):
        """
        Initialize a new course with name, trimester, credits, and max score.
        """
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.max_score = max_score

class GradeBook:
    def __init__(self):
        """
        Initialize the grade book with empty student and course lists.
        """
        self.students = []
        self.courses = {}

    def add_student(self, email, names):
        """
        Add a new student to the grade book. Check for existing email to avoid duplicates.
        """
        if any(s.email == email for s in self.students):
            print("Error: Student with this email already exists.")
        else:
            self.students.append(Student(email, names))
            print("Student added successfully.")

    def add_course(self, name, trimester, credits, max_score):
        """
        Add a new course to the grade book. Ensure the course does not already exist.
        """
        if name in self.courses:
            print("Error: Course already exists.")
        else:
            self.courses[name] = Course(name, trimester, credits, max_score)
            print("Course added successfully.")

    def register_student_for_course(self, email, course_name, grade):
        """
        Register a student for a course by updating their records.
        Handle errors for non-existing students or courses.
        """
        student = next((s for s in self.students if s.email == email), None)
        course = self.courses.get(course_name)

        if student is None:
            print("Error: Student does not exist.")
        elif course is None:
            print("Error: Course does not exist.")
        else:
            student.register_for_course(course_name, grade, course.credits, course.max_score)
            print(f"Student {email} registered for course {course_name}.")

    def calculate_GPA_for_all_students(self):
        """
        Calculate the GPA for all students.
        """
        for student in self.students:
            student.calculate_GPA()
        print("GPA calculated for all students.")

    def calculate_ranking(self):
        """
        Return a sorted list of students based on their GPA.
        """
        return sorted(self.students, key=lambda s: s.GPA, reverse=True)

    def search_by_grade(self, course_name, min_grade, max_grade):
        """
        Find students who have a grade within the specified range for a course.
        """
        return [s for s in self.students if course_name in s.courses_registered and
                min_grade <= s.courses_registered[course_name][0] <= max_grade]

    def generate_transcript(self, email):
        """
        Generate a transcript for a student with their GPA and course details.
        """
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
        """
        Display all courses a student is registered for.
        """
        student = next((s for s in self.students if s.email == email), None)
        if student:
            print(f"Courses for {student.names}:")
            for course, (grade, credits, max_score) in student.courses_registered.items():
                print(f"Course: {course}, Grade: {grade}, Credits: {credits}, Max Score: {max_score}")
        else:
            print("Error: Student not found.")

    def list_all_students(self):
        """
        List all students and the courses they are registered for.
        """
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            print(f"Student: {student.names} (Email: {student.email})")
            if student.courses_registered:
                print("Courses:")
                for course, (grade, credits, max_score) in student.courses_registered.items():
                    print(f"  Course: {course}, Grade: {grade}, Credits: {credits}, Max Score: {max_score}")
            else:
                print("  No courses registered.")

def main():
    """
    Main function to interact with the grade book application.
    """
    grade_book = GradeBook()

    while True:
        print("\nSelect an option below")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA for All Students")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Display Courses for Student")
        print("9. List All Students")
        print("10. Exit")

        choice = input("Choose an action: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            grade_book.add_student(email, names)

        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter credits: "))
            max_score = float(input("Enter max score: "))
            grade_book.add_course(name, trimester, credits, max_score)

        elif choice == '3':
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            grade_book.register_student_for_course(email, course_name, grade)

        elif choice == '4':
            grade_book.calculate_GPA_for_all_students()

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
                for course, (grade, credits, max_score) in transcript['courses'].items():
                    print(f"Course: {course}, Grade: {grade}, Credits: {credits}, Max Score: {max_score}")

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
