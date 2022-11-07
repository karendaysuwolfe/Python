# Name: Karendaysu Wolfe
# Date: 8-24-22
# Course: Intro to Programming with Pyth
# Assignment: Module 5
# Assignment: We will implement "if" statements by modifying our program from Module 3.

# Display a welcome
print("Welcome to Fiber Optic Calculator")

# Get the company name from the user
a = input("What's your Name: ")
print("Welcome, " + a)
name = input("What is the name of your company? ")

# Get the numer of feet of fiber optic to be installed
total_feet = float(input("How many feet of fiber optic cable will be installed? "))

# Evaluate the total cost based upon the number of feet request
if total_feet >= 500:
    cost = total_feet * 0.5
elif total_feet >= 250:
    cost = total_feet * 0.7
elif total_feet >= 100:
    cost = total_feet * 0.8

# Display the calculated information including the numer of feet request and company name
print("............")
print("Calculation in progress")
print("")
print("The total cost will be: " + str(cost))
print("Name of the company: " + name)
print("Thank you " + a + " Have a great day.")

input("press to exit")
