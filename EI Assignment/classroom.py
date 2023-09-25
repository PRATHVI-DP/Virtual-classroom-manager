class Classroom:
    def __init__(self,name):
        self.name = name
        self.students  = []
        self.assignments  = []

class Student:
    def __init__(self,student_id,name):
        self.name = name
        self.student_id = student_id

class Assignments:
    def __init__(self,due_date,title):
        self.title = title 
        self.due_date = due_date
        self.submitted = False

class VirtualClassroomManager:
    def __init__(self):
        self.classrooms = []
        self.students = []
        self.assignments = []

    def add_classroom(self,class_name):
        new_classroom  = Classroom(class_name)
        self.classrooms.append(new_classroom)
        print(f"The {class_name} has been created")

    def add_student(self,student_id,class_name):
        classroom = next((c for c in self.classrooms if c.name ==class_name),None)
        if classroom == None:
            print(f"The mentioned{class_name} is not found")
        student = Student(student_id,f"Student{student_id}")
        classroom.students.append(student)
        self.students.append(student)
        print(f"{student_id} has been placed in {class_name} successfully")

    def schedule_assignment(self,class_name,title,due_date):
        classroom = next((c for c in self.classrooms if c.name==class_name),None)
        if classroom is None:
            print("f Error: {class_name} doesnt exist")
        assignment = Assignments(due_date,title)
        classroom.assignments.append(assignment)
        self.assignments.append(assignment)
        print(f"Assignment for {class_name} has been scheduled ")

    def submit_assignment(self,student_id, class_name , title):
        student = next((c for c in self.students if c.name == student_id ),None)
        if student is None:
            print(f"The {student_id} doesnt exists")
        classroom = next((c for c in self.classrooms if c.name==class_name),None)
        if classroom is None:
            print(f" Error: {class_name} doesnt exist")
        assignmet = next((c for c in self.assignments if c.title==title),None)
        if assignmet is None:
            print(f" Error: {title} doesnt exist")
        self.submitted = True
        print(f"{student_id} in {class_name} has successfully submitted the assignment ")


if __name__ == "__main__":
    manager = VirtualClassroomManager()

    while True:
        user_input = input("Enter command (e.g., 'add_classroom Math', 'add_student 1 Math', 'schedule_assignment Math Homework 2023-09-30', 'submit_assignment 1 Math Homework', 'quit'): ")
        parts = user_input.split()

        if parts[0]== "add_classroom":
            manager.add_classroom(parts[1])
        elif parts[0]== "add_student":
            manager.add_student(parts[1],parts[2])
        elif parts[0]=="schedule_assignment":
            manager.schedule_assignment(parts[1],parts[2],parts[3])
        elif parts[0]== "submit_assignment":
            manager.submit_assignment(parts[1],parts[2],parts[3])
        elif parts[0]=="quit":
            break
        else:
            print("Invalid command")

