def main():
    from sys import argv
    script, filename = argv
    filehand = open(filename)
    count = 0
    line = filehand.readline()
    while line:
        count += 1
        line = filehand.readline()
        print(count)

main()
