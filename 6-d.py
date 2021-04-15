f = open("gasprices.txt")
lines = f.readlines()

Japan = 0
Korea = 0

for line in lines:
    Japan += int(line.split()[0])
    Korea += int(line.split()[1])

str = "Japan average: %f\n" % (Japan / len(lines)) + "Korea average: %f" % (Korea / len(lines))

print(str)

f2 = open("out6.txt", "w")
f2.write(str)