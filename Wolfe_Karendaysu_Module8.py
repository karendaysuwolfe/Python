# Name: Karendaysu Wolfe
# Date: 9-15-22
# Course: Intro to Programming with Pyth
# Assignment: Module 7
# Assignment: write a program that uses a function to convert miles to kilometers.

def miles(mph):
    kilometers = mph * 1.609
    return kilometers

while True:
    try:
        mph = float(input("Enter the number of miles: "))
        break
    except ValueError:
        print("ERROR, Try again, please")

print("Total number of kilometers: ", miles(mph), 'km.')
print("Total number of miles: ", mph, 'mph.')

input('Press enter to exit')
