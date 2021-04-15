f = open("scores.txt")

lines = f.readlines()

f2 = open("result.txt", "a")

for line in lines:
    if int(line) == 75:
        f2.write("%d: *\n" % int(line))

    elif int(line) == 76:
        f2.write("%d: *****\n" % int(line))

    elif int(line) == 79:
        f2.write("%d: **\n" % int(line))

    elif int(line) == 81:
        f2.write("%d: ********\n" % int(line))

    elif int(line) == 82:
        f2.write("%d: ******\n" % int(line))

    elif int(line) == 84:
        f2.write("%d: ***********\n" % int(line))