#Program to check whether a string is a Palindrome or not !

def is_Palindrome(s):
    #check if the String is equal to its reverse 
    return s==s[::-1]

#Example Usages 
string ="madam"

#output whether the string is palindrome or not 

print(is_Palindrome(string))

# output will be Boolean Format True or False