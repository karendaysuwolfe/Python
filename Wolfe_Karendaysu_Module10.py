# Name: Karendaysu Wolfe
# Date : 09-24-22
# Class: Intro to Programming with Pyth.
# Assignment: Module 10
# Description: For this module, we will create a program that performs file processing activities.


# Your program will prompt the user for the directory
# they would like to save the file in as well as the name of the file
import os

# The program should then prompt the user for their name, address, and phone number.
def main():
    directory = input("Enter the Directory that you need to save the file: ")
    filename = input("Enter the filename: ")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")

# the program will write this data to a comma separated line in a file and store
# the file in the directory specified by the user.
    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory, filename), 'w')
        writeFile.write(name + ',' + address + ',' + phone_number + '\n')
        writeFile.close()

        print("File contents:")
# reading the file
        readFile = open(os.path.join(directory, filename), 'r')
        for line in readFile:
            print(line)
        readFile.close()

    else:
        print("Error, this directory does not exist, TRY AGAIN")

main()
input('Press enter to exit')