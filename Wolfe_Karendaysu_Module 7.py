# Name: Karendaysu Wolfe
# Date : 09-07-22
# Class: Intro to Programming with Pyth.
# Assignment: Module 7
# Description: Write a program that uses a while loop to determine
# how long it takes for an investment to double at a given interest rate.

# Enter the input of annualized interest rate and initial investment rate.
invested = float(input("Enter The Initial Investment Amount:  "))
rate = float(input("Enter The Annualized Interest Rate: "))
amount = invested
year = 0
# loop
while amount <= invested * 2:
    amount = amount + amount * rate / 100
    year = year + 1
# Enter the output of the number of years.
print("The number of years it takes an investment to double: %d years" %(year))
input("Press enter to exit")

