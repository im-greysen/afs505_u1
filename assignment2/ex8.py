# establishes the format of 4 arguments in a string?
formatter = "{} {} {} {}"
# crates 4 strings of 4 elements each
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
# prints a string using the 4 lines as the 4 elements
print(formatter.format(
    "Try your",
    "own text here",
    "Maybe a poem",
    "Or a song about fear"
))
