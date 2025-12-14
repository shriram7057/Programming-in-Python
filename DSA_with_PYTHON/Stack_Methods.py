undo_stack = []    # Keeps history of performed actions
redo_stack = []    # Keeps undone actions
text = ""          # The document

# Append action
def append(char):
    global text
    text += char
    undo_stack.append(('append', char))
    redo_stack.clear()  # Whenever you do new change, redo history is invalid

# Undo action
def undo():
    global text
    if not undo_stack:
        print("Nothing to undo.")
        return
    action, char = undo_stack.pop()
    if action == 'append':
        text = text[:-1]
        redo_stack.append((action, char))

# Redo action
def redo():
    global text
    if not redo_stack:
        print("Nothing to redo.")
        return
    action, char = redo_stack.pop()
    if action == 'append':
        text += char
        undo_stack.append((action, char))

# Show current state
def read():
    print(f"Current Text: {text}")

# --- Example Walkthrough ---
append('A')  # text: "A"
append('B')  # text: "AB"
append('C')  # text: "ABC"
undo()       # removes 'C', text: "AB"
read()       # Should print: "AB"
redo()       # adds 'C' back, text: "ABC"
read()       # Should print: "ABC"
