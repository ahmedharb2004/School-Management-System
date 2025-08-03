



from colorama import init, Fore, Style
import os
###################################################
from abc import ABC, abstractmethod

init(autoreset=True)


class Person:
    def __init__(self, ID, name, password):
        self.__ID = ID
        self.__name = name
        self.__password = password

    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def valid_pass(self, password):
        return self.__password == password


class Student(Person):
    def __init__(self, ID, name, password):
        super().__init__(ID, name, password)
        self.__courses = []

    def get_course(self):
        return self.__courses

    def enroll_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)
            print(Fore.GREEN + "✅ Course enrolled successfully.")
        else:
            print(Fore.YELLOW + "⚠️ Already enrolled in this course.")

    def remove_course(self, courseID):
        for course in self.__courses:
            if course.courseID == courseID:
                self.__courses.remove(course)
                print(Fore.GREEN + "✅ Course removed successfully.")
                return
        print(Fore.RED + "❌ Course not found.")


class Course:
    def __init__(self, courseID, courseName, Credits):
        self.courseID = courseID
        self.courseName = courseName
        self.Credits = Credits


class Service:
    def __init__(self):
        self.student = {}

    def add_student(self, student):
        if student.get_ID() in self.student:
            print(Fore.YELLOW + "⚠️ Student already exists.")
        else:
            self.student[student.get_ID()] = student
            print(Fore.GREEN + "✅ Student added successfully.")

    def delete_student(self, ID, password):
        student = self.student.get(ID)
        if student and student.valid_pass(password):
            del self.student[ID]
            print(Fore.GREEN + "✅ Student deleted successfully.")
        else:
            print(Fore.RED + "❌ Invalid data.")

    def get_student(self, ID):
        return self.student.get(ID)

    def list_students(self):
        return list(self.student.values())


class IAuthenticationService(ABC):
    @abstractmethod
    def login(self, student_service, ID, password):
        pass


class AuthenticationService(IAuthenticationService):
    def login(self, student_service, ID, password):
        student = student_service.get_student(ID)
        if student and student.valid_pass(password):
            return student
        return None



student_service = Service()
auth_service = AuthenticationService()



while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(Fore.CYAN + Style.BRIGHT + "\n╔══════════════════════════════════════╗")
    print("║        School Management System      ║")
    print("╚══════════════════════════════════════╝")
    print(Fore.YELLOW + "1. ➕ Add Student")
    print("2. 📚 Enroll in Course")
    print("3. ❌ Remove Course")
    print("4. 👁️ Show Student Info")
    print("5. 🗑️ Delete Student")
    print("0. 🚪 Exit")
    print(Fore.LIGHTBLACK_EX + "-" * 40)

    choice = input(Fore.WHITE + "👉 Enter your choice (0-5): ")

    print(Fore.LIGHTBLACK_EX + "-" * 40)

    if choice == "1":
        id = input("🆔 Enter ID: ")
        name = input("📛 Enter Name: ")
        password = input("🔑 Enter Password: ")
        student = Student(id, name, password)
        student_service.add_student(student)

    elif choice == "2":
        id = input("🆔 Enter your ID: ")
        password = input("🔑 Enter your password: ")
        student = auth_service.login(student_service, id, password)
        if student:
            course_id = input("📘 Course ID: ")
            course_name = input("📗 Course Name: ")
            credits = int(input("💠 Credits: "))
            course = Course(course_id, course_name, credits)
            student.enroll_course(course)
        else:
            print(Fore.RED + "❌ Login failed.")

    elif choice == "3":
        id = input("🆔 Enter your ID: ")
        password = input("🔑 Enter your password: ")
        student = auth_service.login(student_service, id, password)
        if student:
            course_id = input("❌ Enter Course ID to remove: ")
            student.remove_course(course_id)
        else:
            print(Fore.RED + "❌ Login failed.")

    elif choice == "4":
        id = input("🆔 Enter your ID: ")
        password = input("🔑 Enter your password: ")
        student = auth_service.login(student_service, id, password)
        if student:
            print(Fore.MAGENTA + f"\n👤 Student Info:")
            print(f"   🆔 ID: {student.get_ID()}")
            print(f"   📛 Name: {student.get_name()}")
            print("   📘 Enrolled Courses:")
            if student.get_course():
                for c in student.get_course():
                    print(f"     - {c.courseName} [{c.courseID}] ({c.Credits} credits)")
            else:
                print("     🔕 No courses enrolled.")
        else:
            print(Fore.RED + "❌ Login failed.")

    elif choice == "5":
        id = input("🆔 Enter ID: ")
        password = input("🔑 Enter Password: ")
        student_service.delete_student(id, password)

    elif choice == "0":
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Goodbye! Have a nice day!")
        break

    else:
        print(Fore.RED + "❌ Invalid choice. Please try again.")

    input(Fore.LIGHTBLACK_EX + "\n🔁 Press Enter to continue...")
