for i in range(1, 5):
    print(*('*' * i), sep=' ', end='\n')


# sep=' ' ensures spaces between stars.
# end='\n' moves to the next line after printing each row.
# *('*' * i) unpacks the string so that each character is treated as a separate argument.
# '*' * i creates a string with i stars