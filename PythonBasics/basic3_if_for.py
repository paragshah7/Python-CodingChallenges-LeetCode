# coding=utf-8
name = "Liverpool"
if not name:
    print("1 - Name is empty")

age = 22
if age >= 18:
    print("2 - Eligible")
else:
    print("2 - Not eligible")

condition = None
if condition:
    print("3 - is True")
else:
    print("3 - is False")

# one liner if condition
age2 = 12
message2 = "Eligible" if age2 >= 18 else "Not eligible"
print("4 - ", message2)


# Search in a list using for-else loop
def for_search():
    names = ["Apple", "Banana"]
    for name in names:
        if name.startswith("A"):
            print("5 - Found")
            break
    else:
        print("5 - Not found")

    nums = [1, 2, 3, 4, 5]
    for num in nums:
        if num == 4:
            print("Break the loop", num)
            break
        if num == 3:
            print("Found", num, "but continue")
            continue
        print(num)


for_search()


def for_print():
    for x in "Python":
        print(x)
    for x in range(0, 10, 2):     # Range is the function name, 2 is the interval
        print(x)


# for_print()
