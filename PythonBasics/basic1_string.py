print("Hello Parag \n")

print("Cool " * 10)

# separate lines
mul_str = """
Hi
You can use triple quotes 
to add multiple lines
"""
print(mul_str)

x, y = 1, 2

print(type(1.1))
print(type('True'))

message = "San Francisco"
print(len(message))
print(message[0:5])
print(message.find("o"))

# Placehoders
greeting = 'Hi'
name = 'Sandy'

new_message = '{}, {}. Welcome!'.format(greeting, name)
new_message2 = f'{greeting}, {name}. Welcome to f string!'     # f strings, new way to write strings

print(new_message)
print(new_message2)

# # number
# x = input("x: ")
# print(int(x))
# print(float(x))
# print(bool(x))

# getting value from a string
name = "Hello"
print(name[0], name[-1])
print(name[0:3])

# expression
first = "Parag"
last = "shah"
full = f"{first} {last}"
print(full)

# String functions
print(full.title())
print(full.find("Parag"))   # at which location the start element of the string is
print(full.replace("P", "p"))
print("Parag" in full)

# help(str)
