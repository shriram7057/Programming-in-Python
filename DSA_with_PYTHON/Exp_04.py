class StudentNode:
    """Represents a single student record node in the linked list."""
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None

class StudentLinkedList:
    """Implements the singly linked list for student records."""
    def __init__(self):
        self.head = None

    # 1. Add Student (Insertion at the end)
    def add_student(self, roll_no, name, marks):
        new_node = StudentNode(roll_no, name, marks)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print("\nStudent record added.")

    # 2. Delete Student (Corrected logic for head and intermediate nodes)
    def delete_student(self, roll_no):
        current = self.head
        prev = None

        # Case 1: Head node is the target
        if current and current.roll_no == roll_no:
            self.head = current.next
            print("\nStudent record deleted.")
            return

        # Case 2: Search for the node to delete
        while current and current.roll_no != roll_no:
            prev = current
            current = current.next

        # Case 3: Student not found
        if current is None:
            print("\nStudent not found.")
            return

        # Case 4: Node found (current is the target, prev is the node before it)
        if prev:
            prev.next = current.next # Link previous node to next node
        
        print("\nStudent record deleted.")

    # 3. Update Student (Corrected: uses explicit new_name/new_marks)
    def update_student(self, roll_no, new_name, new_marks):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                current.name = new_name
                current.marks = new_marks
                print("\nStudent record updated.")
                return
            current = current.next
        print("\nStudent not found.")

    # 4. Search Student
    def search_student(self, roll_no):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                print(f"\nFound: Roll No: {current.roll_no}, Name: {current.name}, Marks: {current.marks}")
                return
            current = current.next
        print("\nStudent not found.")
    
    # 5. Display All Students
    def display_students(self, sort_by="roll_no", ascending=True):
        students = []
        current = self.head
        
        # 1. Collect all student data into a list
        while current:
            # Store as a tuple: (Roll No, Name, Marks)
            students.append((current.roll_no, current.name, current.marks))
            current = current.next

        if not students:
            print("\nNo records to display.")
            return

        # 2. Sort the collected list based on key and order
        if sort_by == "roll-no":
            # Sort by Roll No (index 0)
            students.sort(key=lambda x: x[0], reverse=not ascending)
        elif sort_by == "marks":
            # Sort by Marks (index 2)
            students.sort(key=lambda x: x[2], reverse=not ascending)

        # 3. Display sorted records
        print("\nStudent Records:")
        for s in students:
            print(f"Roll No: {s[0]}, Name: {s[1]}, Marks: {s[2]}")

# Menu for interaction 
def menu():
    system = StudentLinkedList()
    while True:
        print("\n--- Student Record Management Menu ---")
        print(" 1. Add Student")
        print(" 2. Delete Student")
        print(" 3. Update Student")
        print(" 4. Search Student")
        print(" 5. Display All Students")
        print(" 6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            try:
                roll = int(input("Enter Roll No: "))
                name = input("Enter Name: ")
                marks = int(input("Enter Marks: "))
                system.add_student(roll, name, marks)
            except ValueError:
                print("\nInvalid input for Roll No or Marks.")

        elif choice == '2':
            try:
                roll = int(input("Enter Roll No to Delete: "))
                system.delete_student(roll)
            except ValueError:
                print("\nInvalid input for Roll No.")

        elif choice == '3':
            try:
                roll = int(input("Enter Roll No to update: "))
                name = input("Enter New Name: ")
                marks = int(input("Enter New Marks: "))
                system.update_student(roll, name, marks)
            except ValueError:
                print("\nInvalid input for Roll No or Marks.")

        elif choice == '4':
            try:
                roll = int(input("Enter Roll No to search: "))
                system.search_student(roll)
            except ValueError:
                print("\nInvalid input for Roll No.")

        elif choice == '5':
            sort_key = input("Sort by 'roll-no' or 'marks': ").strip().lower()
            order = input("Order 'asc' or 'desc': ").strip().lower()
            ascending = True if order == 'asc' else False
            
            if sort_key not in ['roll-no', 'marks']:
                print("\nInvalid sort key. Defaulting to 'roll-no' ascending.")
                sort_key = 'roll-no'

            system.display_students(sort_by=sort_key, ascending=ascending)

        elif choice == '6':
            print("\nExiting Student Record Management System.")
            break
        else:
            print("\nInvalid choice. Try again.")

# Start the System
menu()