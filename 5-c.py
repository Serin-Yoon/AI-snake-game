MAX_VALUE = 3

print("#" + "=" * 16 + "#")

for i in range(MAX_VALUE + 1):
    print("|" + " " * ((3 - i) * 2) + "<>" + "." * (i * 4) + "<>" + " " * ((3 - i) * 2) + "|")

for i in range(MAX_VALUE, 0, -1):
    print("|" + " " * ((3 - i) * 2) + "<>" + "." * (i * 4) + "<>" + " " * ((3 - i) * 2) + "|")

print("#" + "=" * 16 + "#")