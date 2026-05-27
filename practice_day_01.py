# Variables, Strings, and Basic Logic (Python)


# Swap two variables without using a third variable.

a= int(input("Enter a : "))
b = int (input("Enter b : "))

a = a + b 
b = a - b 
a = a - b

print("a is : " , a)
# print("b is : ", b)

# Take a user's full name and print it in "Lastname, Firstname" format.

first_name = input("Enter user's first name : ")
last_name = input("Enter user's last name : ")

last_name , first_name = first_name , last_name
print(first_name , last_name)

# Calculate the area of a circle where the radius is taken as user input.

radius = float(input("Enter the radius: "))
area = 3.1416*radius*radius
print("the area is : " , area)

# Create a program that converts Celsius to Fahrenheit.

celsius = float(input("Enter the cels' temp : "))
fahernheit = (celsius *9 / 5) + 32
print("the fahernheit temp is :", fahernheit)

# Input a sentence and count how many words it has using split().

sent = input("Enter any sentence : ")
count = len(sent.split())
print(count)

# Take a string and print it in reverse without using loops (use slicing).

str = input("Enter string : ")
reverse_str = str[:: -1]
print(reverse_str)

# Check if a string is a palindrome (reads the same forward and backward).'

str = input("enter string :")
reverse_str = str[::-1]
if(reverse_str == str):
    print("palindrome")
else:
    print("Not palindrome")
            
# Extract the domain name from an email address (e.g., user@gmail.com → gmail.com).
email = input("enter the string : ")
if('@' in email):
    pos = email.find('@')
    domain = email[pos + 1 :]
    print(domain)
else:
    print("no domain exist")    

# Remove all leading and trailing spaces from a string and replace middle spaces with hyphens.

str = input("Enter sting : ")
new_str = str.strip()
if(' ' in new_str):
    new_new_str = new_str.replace(' ' , '-')
    print(new_new_str)
    
# Input a long string and find the index of a specific word.

str = input("Enter string : ")

target_str = input("your target string : ")

index_pos=str.find(target_str)
print(index_pos)


# Demonstrate the difference between / and // operators with examples.

# Calculate the power of a number (a 
# b
#  ) using the ** operator.

# Print a string 10 times without using a loop (use string multiplication).

# Create an f-string that displays a float with exactly 2 decimal places.

# Use escape characters to print: I'm learning "Python" today.

# Take a number and check if it’s a multiple of both 3 and 5.

# Write a program that takes a price and a discount percentage, then prints the final price.

# Get a character from the user and print its ASCII value using ord().

# Take a 3-digit number and find the sum of its digits (e.g., 123→1+2+3=6).

# Check if a given year is a leap year using only one if statement with logical operators.

# Input a string and capitalize only the first and last characters.

# Create a basic calculator that takes two numbers and an operator (+,−,∗,/).

# Find the remainder of a division without using the % operator.

# Check if a string contains only numbers.

# Convert a string like "1,000" into an integer (remove the comma).

# Take a user's birth year and calculate their age.

# Swap the first and last characters of a string.

# Repeat a string N times, where N is provided by the user.

# Use input() to get a sentence and replace all vowels with *.

# Write a program that converts total seconds into hours, minutes, and seconds.

