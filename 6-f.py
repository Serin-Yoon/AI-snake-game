f = open("movies.txt")
lines = f.readlines()

word = input("Search word? ")

cnt = 0
for line in lines:
    if word in line or word.upper() in line or word.lower() in line or word.capitalize() in line or word.swapcase() in line:
        cnt += 1
        print(line[:-1])

print("%d matches." % cnt)