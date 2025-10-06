"""
This program calculates the sum of the first 10 natural numbers.
Natural numbers start from 1, so we consider numbers from 1 to 10.
The formula for the sum of the first N natural numbers is:
Sum = N * (N + 1) / 2
"""

# Define the number of natural numbers to sum
N = 10

# Calculate the sum using the formula
sum_natural = N * (N + 1) // 2  # Using integer division

# Print the result
print("Sum of first 10 natural numbers:", sum_natural)
