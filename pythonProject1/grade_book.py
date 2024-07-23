class Student:
    """A class representing a student."""

    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = {}
        self.GPA = 0.0

    def register_for_course(self, course, grade):
        """
        Register the student for a course with a given grade.

        Parameters:
            course (str): The name of the course.
            grade (float): The grade received in the course.
        """
        self.courses_registered[course] = grade

    def calculate_GPA(self):
        """
        Calculate the student's GPA based on the registered courses.

        Returns:
            float: The GPA of the student.
        """
        if not self.courses_registered:
            self.GPA = 0.0
            return self.GPA
        total_points = sum(self.courses_registered.values())
        num_courses = len(self.courses_registered)
        self.GPA = total_points / num_courses
        return self.GPA


class Course:
    """
    A class representing a course.

    Attributes:
        name (str): The name of the course.
        trimester (str): The trimester in which the course is offered.
        credits (int): The number of credits for the course.
    """

    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits


class GradeBook:
    """
    A class representing a grade book for managing students and courses.

    Attributes:
        student_list (list): A list of students.
        course_list (list): A list of courses.
    """

    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student):
        """
        Add a student to the grade book.

        Parameters:
            student (Student): The student to be added.
        """
        self.student_list.append(student)

    def add_course(self, course):
        """
        Add a course to the grade book.

        Parameters:
            course (Course): The course to be added.
        """
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name, grade):
        """
        Register a student for a course with a given grade.

        Parameters:
            student_email (str): The email of the student.
            course_name (str): The name of the course.
            grade (float): The grade received in the course.
        """
        student = self.find_student_by_email(student_email)
        if student:
            student.register_for_course(course_name, grade)

    def calculate_GPA(self):
        """
        Calculate GPA for all students in the grade book.
        """
        for student in self.student_list:
            student.calculate_GPA()

    def calculate_ranking(self):
        """
        Calculate and return the ranking of students based on their GPA.

        Returns:
            list: A sorted list of students by GPA in descending order.
        """
        return sorted(self.student_list, key=lambda x: x.GPA, reverse=True)

    def search_by_grade(self, course_name, grade_range):
        """
        Search students by grade obtained in a course within a given range.

        Parameters:
            course_name (str): The name of the course.
            grade_range (range): The grade range to search for.

        Returns:
            list: A list of students who have grades within the given range.
        """
        result = []
        for student in self.student_list:
            grade = student.courses_registered.get(course_name)
            if grade in grade_range:
                result.append(student)
        return result

    def generate_transcript(self, student_email):
        """
        Generate a transcript for a student showing their GPA and registered courses.

        Parameters:
            student_email (str): The email of the student.

        Returns:
            str: The transcript of the student.
        """
        student = self.find_student_by_email(student_email)
        if student:
            transcript = (f"Transcript for {student.names}\n"
                          f"Email: {student.email}\n"
                          f"GPA: {student.GPA}\n"
                          f"Courses:\n")
            for course, grade in student.courses_registered.items():
                transcript += f"{course}: {grade}\n"
            return transcript
        return "Student not found."

    def find_student_by_email(self, email):
        """
        Find a student by their email.

        Parameters:
            email (str): The email of the student.

        Returns:
            Student: The student with the given email, or None if not found.
        """
        for student in self.student_list:
            if student.email == email:
                return student
        return None
