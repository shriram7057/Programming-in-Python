def generate_pascals_triangle(rows):
    triangle = []  # List to store Pascal’s Triangle

    for i in range(rows):
        row = [1]  # First element of each row is always 1
        if i > 0:
            for j in range(1, i):
                # Sum of the two elements above in the previous row
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(50))  # Center alignment for better display

# Input number of rows from user
num_rows = int(input("Enter the number of rows: "))

# Generate and display Pascal’s Triangle
triangle = generate_pascals_triangle(num_rows)
print_pascals_triangle(triangle)
