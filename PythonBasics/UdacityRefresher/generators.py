def all_even():
    n = 0
    while True:
        yield n  # all even is a generator because yield is used.
        # it pauses the fn and returns a value every time next is called
        n += 2


my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

# Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)

# Now go back to generating more even numbers.
for i in range(100):
    print(next(my_gen))
