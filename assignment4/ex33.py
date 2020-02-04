i = 0
numbers = []

numb = 36
three = 3

while i < numb + three:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += three
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
