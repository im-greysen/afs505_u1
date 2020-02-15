def main():

    from sys import argv
    script, filename = argv
    filehand = open(filename)
    count = 0
    line = filehand.readline()
    words = len(line.split())
    chars = len(line)


    while line:
        count += 1
        line = filehand.readline()
        words += len(line.split())
        chars += len(line)
    print()
    print(f"""    There are {count} lines
    There are {words} words.
    There are {chars} characters.
    The name of the file is {filename}""")
    print()


main()
