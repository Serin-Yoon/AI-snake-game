from random import *

n1 = randint(1, 6)
n2 = randint(1, 6)

while n1 + n2 != 7:
    print("%d + %d = %d" % (n1, n2, n1 + n2))
    n1 = randint(1, 6)
    n2 = randint(1, 6)

print("%d + %d = %d" % (n1, n2, n1 + n2))