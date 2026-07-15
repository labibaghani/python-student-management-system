students = []

class Student:
       
    def __init__(self,name,roll_no,age,department,cgpa):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.department = department
        self.cgpa = cgpa

    def display(self):
        print("-" * 25)
        print(f"Name       : {self.name}")
        print(f"Roll No    : {self.roll_no}")
        print(f"Age        : {self.age}")
        print(f"Department : {self.department}")
        print(f"CGPA       : {self.cgpa}")
        print("-" * 25)

# student1 = Student("Labiba", "23-CS-101", 20, "Computer Science", 3.75)
# student1.display()

# student2 = Student("Ali", "23-CS-102", 21, "SE", 3.5)
# student2.display()

while True:
    print("-" * 25)
    print("STUDENT MANAGEMENT SYSTEM")
    print("-" * 25)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice in ["1","2","3","4","5"]:
     
        if choice=="1":
         
         try:
            name = input("Enter Name: ")
            roll_no = input("Enter Roll No: ")

            age = int(input("Enter Age: "))
            if age <= 0:
                print("Age must be greater than 0")
                continue

            department = input("Enter Department: ")
        
            cgpa = float(input("Enter CGPA: "))
            if cgpa < 0 or cgpa > 4:
                print("CGPA must be between 0.0 and 4.0")
                continue

            student = Student(name, roll_no, age, department, cgpa)
            students.append(student)
            print("Student added successfully!")

         except ValueError:
              print("Please enter a valid number.")

        elif choice == "2":

            if len(students) == 0:
                print("No students found.")
            else:
                for student in students:
                    student.display()

        elif choice == "3":

            if len(students) == 0:
                print("No students found.")
                
            search_roll = input("Enter Roll Number: ")
            found = False

            for student in students:
                if student.roll_no == search_roll:
                    student.display()
                    found = True
                
            if not found:
                    print("Student not found.")
            
        elif choice == "4":
            
            if len(students) == 0:
                print("No students found.")

            delete_roll = input("Enter Roll Number: ")
            found = False

            for student in students:
                if student.roll_no == delete_roll:
                    students.remove(student)
                    found = True
                    print("Student Removed Successfully!")
                    break
            
            if not found:
                    print("Student not found.")
            


        elif choice=="5":

            print("Thank You!!")
            break
    
    else:
        print("Invalid choice! Choose 1,2,3,4 or 5")

    