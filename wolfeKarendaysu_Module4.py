# Name: Karendaysu Wolfe
# Date: 8-19-22
# Course: Intro to Programming with Pyth
# Assignment: Module 4


# Initialize with values
names = ['Arthur', 'Nick', 'Lisa', 'Ana', 'Luis', 'Jose', 'Judith', 'Roxy', 'Camila', 'Jake', 'Sam', 'Aurelio',
         'Angel', 'Maia', 'Aitana']

# Display the contents in a single statement
print("Tuple with names:")
print(names)

print('------------End of Loop---------------')

# Iterate through the collection displaying the output as a single complete sentence for each value.
for name in names:
    print(f"My name is {name}.")

print('------------End of Loop---------------')

# Repeat the output in reverse order using a different context string.
for name in reversed(names):
    print(f"My name is not {name}.")

print()

input("press enter to exit")