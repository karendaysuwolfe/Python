# Name: Karendaysu Wolfe
# Date: 09-02-22
# Course: Intro to Programming with Pyth
# Assignment: Module 6
# Create a program that includes a dictionary of a topic that interest you.

# keys and values pairs
myrammsteinfavoritesongs= {'song1': 'Deutschland', 'song2': 'Mein Herz Brennt','song3': ' Engel', 'song4': 'Dicke Titten',
                           'song5': 'Amour', 'song6': 'Du Hast', 'song7': 'Du Riechst So Gut',
                           'song8': 'Amerika', 'song9': 'Rosenrot', 'song10': 'Angst'}

# Prints keys and values pairs
print("My Rammstein dictory: \n", myrammsteinfavoritesongs)

# Select a key
a=input("Select your favorite Rammstein song: ")

# Prints your key that you selected
print("You're favorite Rammstein song is: ", myrammsteinfavoritesongs[a])
input("press enter to exit")