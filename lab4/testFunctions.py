import copy

import numpy as np
from utils import fitness
import random


def krzyzowanie(population):
    samples = random.sample(population,2)
    par1 = samples[0]
    par2 = samples[1]

    startIndx = random.randrange(0,len(par1)-1)
    length = random.randrange(startIndx, len(par1)-1)

    slice = []
    for i in range(length):
        slice.append(par1[i+startIndx])

    # print(par1)
    # print(par2)
    # print(slice)

    offspring = copy.deepcopy(par2)
    # delete slice from par2
    for i in range(len(slice)):
        for j in range(len(offspring)):
            if slice[i] == par2[j]:
                offspring.pop(j)
    newPerson = np.insert(offspring, startIndx, slice)

    # return newPerson
    return population



population = [[1,2,3,4,5],[2,4,6,8,10],[3,6,9,12,15]]
krzyzowanie(population)


