class Course:
    def __init__(self, course_code, title, max_capacity):
        self.course_code = course_code
        self.title = title
        self.max_capacity = max_capacity
        self.num_of_enrolled_students = []

    def add_student(self, student):
        if len(self.num_of_enrolled_students) < self.max_capacity:
            self.num_of_enrolled_students.append(student)
            print(f"Student {student.name} successfully enrolled in {self.title}.")
        else:
            print(f"Enrollment failed. {self.title} is already at maximum capacity.")

    def get_enrolled_students(self):
        return self.num_of_enrolled_students

    def get_current_enrollment(self):
        return len(self.num_of_enrolled_students)

    def display_course_details(self):
        print(f"Course Code: {self.course_code}")
        print(f"Title: {self.title}")
        print(f"Max Capacity: {self.max_capacity}")
        print(f"Current Enrollment: {self.get_current_enrollment()}")
        print(f"Enrolled Students: {', '.join(student.name for student in self.num_of_enrolled_students)}")
        print("\n")

    def to_string(self):
        enrolled_students_names = [student.name for student in self.num_of_enrolled_students]
        return f"{self.course_code},{self.title},{self.max_capacity},{','.join(enrolled_students_names)}\n"


class Student:
    def __init__(self, name):
        self.name = name
        self.enrolled_courses = []

    def enroll_in_course(self, course):
        course.add_student(self)
        self.enrolled_courses.append(course)
        print(f"{self.name} successfully enrolled in {course.title}.")

    def get_enrolled_courses(self):
        return self.enrolled_courses

    def display_student_info(self):
        one=len(self.name)
        print(f"Name: {self.name}\nid:{one}")
        print("Enrolled Courses:")
        for course in self.enrolled_courses:
            print(f"  - {course.title}")
        print("\n")

    def to_string(self):
        enrolled_courses_titles = [course.title for course in self.enrolled_courses]
        return f"{self.name},{','.join(enrolled_courses_titles)}\n"


def write_data_to_file(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(item.to_string())


def read_courses_from_file(filename):
    courses = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            course_code, title, max_capacity, num_of_enrolled_students = data[0], data[1], int(data[2]), data[3:]
            course = Course(course_code, title, max_capacity)
            courses.append(course)
            for student_name in num_of_enrolled_students:
                student = Student(student_name)
                course.add_student(student)
    return courses


def read_students_from_file(filename, all_courses):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            name, enrolled_courses_titles = data[0], data[1:]
            student = Student(name)
            students.append(student)
            for course_title in enrolled_courses_titles:
                for course in all_courses:
                    if course.title == course_title:
                        student.enroll_in_course(course)
                        break
    return students


# Example usage:
if __name__ == "__main__":
    # Creating Course instances
    cs_course = Course("CS", "Computer Science", 2)
    math_course = Course("MATH", "Mathematics", 1)

    # Creating a list of courses
    all_courses = [cs_course, math_course]

    # Writing courses to file
    write_data_to_file(all_courses, "courses.txt")

    # Reading courses from file
    read_courses = read_courses_from_file("courses.txt")

    # Displaying course details after reading from file
    for course in read_courses:
        course.display_course_details()

    # Creating Student instances
    Umaru = Student("Umaru")
    bobi = Student("Bobi")

    # Creating a list of students
    all_students = [Umaru, bobi]

    # Enrolling students in courses
    Umaru.enroll_in_course(cs_course)
    bobi.enroll_in_course(math_course)

    # Writing students to file
    write_data_to_file(all_students, "students.txt")

    # Reading students from file
    read_students = read_students_from_file("students.txt", all_courses)

    # Displaying student information after reading from file
    for student in read_students:
        student.display_student_info()