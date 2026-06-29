class Student:
    def __init__(self, name, roll_no, section):
        self.name = name
        self.roll_no = roll_no
        self.section = section

class StudentManagement:
    def __init__ (self) :
        self.students = []
        

    def add_student(self, student) :
        for existing_student in self.students :
             if student.roll_no == existing_student.roll_no:
                 print("Student already exists")
                 break
        else :
            self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f"{student.name} | {student.roll_no} | {student.section}")

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no :
                print(f"Student with roll_no {roll_no} is {student.name}")
                break
        else :
            print("Student Not Found")

    def update_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                new_name = input("Enter the new name of the student: ")
                new_section = input("Enter the new section of the student: ")
                student.name = new_name
                student.section = new_section
                print("Student updated successfully")
                break
        else :
            print("Roll no does not exist")
              

    def remove_student(self, roll_no) :
        for student in self.students :
            if student.roll_no == roll_no:
                self.students.remove(student)
                break
        else :
            print("Student not found")

management = StudentManagement()

while True :

    print("1. Add Student")
    print("2. Display students")
    print("3. Search Students")
    print("4. Remove students")
    print("5. Update Student")
    print("6. Exit ")

    choice = input("Enter your choice: ")

    if choice == '1' :
        name = input("Enter the name of the student: ")
        roll_no = int(input("Enter the roll_no of the student: "))
        section = input("Enter the section of the student: ")

        new_student = Student(name,roll_no,section)
        management.add_student(new_student)

    elif choice == '2' :
        management.display_students()

    elif choice == '3' :
        roll_no = int(input("Enter the roll no of the student: "))
        management.search_student(roll_no)

    elif choice == '4':
        roll_no = int(input("Enter the roll no of the student: "))
        management.remove_student(roll_no)

    elif choice == '5' :
        roll_no = int(input("Enter the roll no of the student to update: "))
        management.update_student(roll_no)

    elif choice == '6' :
        print("Exiting the program")
        break

    else :
        print("Invalid choice")
   






    

          


    
    