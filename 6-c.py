f = open("hours.txt")

lines = f.readlines()

for line in lines:
    ID, ClassName, h1, h2, h3, h4, h5 = line.split()
    hours = float(h1) + float(h2) + float(h3) + float(h4) + float(h5)
    print("%s ID %s worked %f hours: %f / day" % (ClassName, ID, hours, hours / 5))
