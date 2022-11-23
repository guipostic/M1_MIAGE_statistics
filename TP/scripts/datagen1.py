import random
import math

for i in range(0,150):
    n = random.randint(1,100)
    factor = random.randint(0,50)
    factor = 1 + factor/(n+50)
    logn = math.log(n)
    logn = logn*factor

    print(n, logn)


