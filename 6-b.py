def input_stats(fileName):
    f = open(fileName)
    lines = f.readlines()
    max = 0
    maxLine = ''
    for line in lines:
        if len(line) >= max:
            max = len(line)
            maxLine = line
    print("Longest line = %d" % max)
    print(maxLine)

input_stats("hours.txt")