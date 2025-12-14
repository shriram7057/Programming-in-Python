# Undo/Redo System using Stack in Python
class TextEditor:
    def __init__(self):
        self.document = ""  # Current state of the document 
        self.undo_stack = []  # Stores previous document states [cite: 59]
        self.redo_stack = []  # Stores states that were undone [cite: 60]

    # Make a new change
    def make_change(self, change):
        # Store the current state (before the change) to the undo stack [cite: 65]
        self.undo_stack.append(self.document)
        
        # Apply the new change [cite: 66]
        self.document += change
        
        # Clear the redo stack, as any new change invalidates undone actions [cite: 66]
        self.redo_stack.clear()
        
        print("\nChange made.")
        self.display_state()

    # Undo last change
    def undo_action(self):
        if self.undo_stack:
            # Move current state (before revert) to redo stack for potential redo [cite: 75]
            self.redo_stack.append(self.document)
            
            # Revert to the last state from the undo stack [cite: 75]
            self.document = self.undo_stack.pop()
            
            print("\nUndo performed.")
        else:
            print("\nNo more action to undo.")
        self.display_state()

    # Redo last undone change
    def redo_action(self):
        if self.redo_stack:
            # Move current state (before re-apply) to undo stack [cite: 87]
            self.undo_stack.append(self.document)
            
            # Re-apply the last undone state from the redo stack [cite: 91]
            self.document = self.redo_stack.pop()
            
            print("\nRedo performed.")
        else:
            print("\nNo more actions to redo.")
        self.display_state()

    # Display current document state
    def display_state(self):
        print("Current Document State: '" + self.document + "'")

    # Run the editor (menu-driven)
    def run_editor(self):
        while True:
            print("\n--- MENU ---")
            print("1. Make a Change")
            print("2. Undo")
            print("3. Redo")
            print("4. Display Document State")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                change = input("Enter text to add: ")
                self.make_change(change)
            elif choice == '2':
                self.undo_action()
            elif choice == '3':
                self.redo_action()
            elif choice == '4':
                self.display_state()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")

# Run the editor
editor = TextEditor()
# CORRECTION: Uncomment the line below to start the program's menu loop
editor.run_editor()