import random
import numpy

sucet = 1
sucin = 1
zoznam = []
while 2 * sucet != sucin:
    zoznam = (random.sample(range(1, 100000), 2021))
    sucet = sum(zoznam)
    sucin = numpy.prod(zoznam)
print(max(zoznam))