


    km = miles*
while not kilometers:
    try:
        kilometers = float(input('Enter the number of miles: '))
    except ValueError:
        print("Error, That's not a valid number")


conversion = 0.62137119

miles = kilometers / conversion
print(' Total Number of Kilometers: ', miles, 'km')
print('Total Number Of Miles: ', kilometers, 'mph')
input('Please press enter to exit')





