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

try:
    with open("students.txt", "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split(",")

            name = parts[0]
            roll_no = parts[1]
            age = int(parts[2])
            department = parts[3]
            cgpa = float(parts[4])
            
            student = Student(name, roll_no, age, department, cgpa)
            students.append(student)

except FileNotFoundError:
    pass

while True:
    print("-" * 25)
    print("STUDENT MANAGEMENT SYSTEM")
    print("-" * 25)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice in ["1","2","3","4","5","6"]:
     
        if choice=="1":
         
         try:
            name = input("Enter Name: ")

            roll_no = input("Enter Roll No: ")
            duplicate = False
            for student in students:
                if student.roll_no == roll_no:
                    print("Roll number already exists.")
                    duplicate = True
                    break
            if duplicate:
             continue

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
            print("")

         except ValueError:
              print("Please enter a valid number.")

        elif choice == "2":

            if len(students) == 0: 
            # if not students:
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
        
        elif choice == "5":

            if len(students) == 0:
                print("No students found.")
                continue

            update_roll = input("Enter Roll Number: ")
            found = False

            for student in students:

                if student.roll_no == update_roll:
                 try:
                    student.name = input("Enter New Name: ")

                    student.age = int(input("Enter New Age: "))
                    if student.age <= 0:
                        print("Age must be greater than 0.")
                        break

                    student.department = input("Enter New Department: ")

                    student.cgpa = float(input("Enter New CGPA: "))
                    if student.cgpa < 0 or student.cgpa > 4:
                        print("CGPA must be between 0.0 and 4.0")
                    
                 except ValueError:
                     print("Please enter a valid number.")
                     break

                 found = True
                 print("Student updated successfully!")
                 break

            if not found:
                print("Student not found.")
                        


        elif choice=="6":
            
            with open("students.txt", "w") as f:
                for student in students:
                    f.write(f"{student.name},{student.roll_no},{student.age},{student.department},{student.cgpa}\n")

            print("Student data saved successfully.")
            print("Thank you for using the Student Management System!")
            break
    
    else:
        print("Invalid choice! Choose 1, 2, 3, 4, 5 or 6.")

    