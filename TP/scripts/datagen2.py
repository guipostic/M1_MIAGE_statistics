from numpy.random import seed
from numpy.random import normal

#make this example reproducible
seed(1)

#generate sample of 200 values that follow a normal distribution 
data = normal(loc=45, scale=23, size=584)

for value in data:
    print(value)
