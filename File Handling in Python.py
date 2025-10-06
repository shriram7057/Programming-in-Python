import os

file_name = "demo.txt"

# 1. Create and write using write() and writelines()
f = open(file_name, "w")
f.write("Line 1: Hello world!\n")
f.write("Line 2: Python is fun.\n")
lines = ["Line 3: This is line 3.\n", "Line 4: This is line 4.\n"]
f.writelines(lines)
f.close()

# 2. Read entire file with read()
f = open(file_name, "r")
print("Reading with read():")
print(f.read())
f.close()

# 3. Read line by line using readline() and readline(size)
f = open(file_name, "r")
print("Reading with readline():")
print(f.readline())  # Reads first line
print("Reading with readline(size=10):")
print(f.readline(10))  # Reads up to 10 characters from second line
f.close()

# 4. Read all lines into a list using readlines()
f = open(file_name, "r")
print("Reading with readlines():")
all_lines = f.readlines()
print(all_lines)
f.close()

# 5. Truncate the file to shorten it
f = open(file_name, "r+")
f.truncate(40)  # Keep only first 40 bytes
f.close()

# 6. Show file after truncate
f = open(file_name, "r")
print("After truncate():")
print(f.read())
f.close()

