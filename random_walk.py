#!/usr/bin/python
#----------------------------------------------------------------------------
# Created By  : Aleksandar Radovanovic
# Created Date: 2022-07-21
# version ='1.0'
# ---------------------------------------------------------------------------

import math
import random
import numpy as np
import matplotlib.pyplot as plt

# random walk test
# A random walk is the random walk on the integer number line
# which starts at 0, and at each step moves -1 for bit 0 or +1 for bit 1
# For a random sequence of bits, random walk should end at 0
# https://en.wikipedia.org/wiki/Random_walk
#--------------------------------------------
def random_walk(rnd_seq):

    positions = [0]
    step = 0

    for i in range( len(rnd_seq) ):
        if rnd_seq[i] == '0':
            step = -1
        else:
            step = 1       
        
        positions.append(positions[i] + step)
    plt.plot(positions)
    plt.xlabel('distance')
    plt.ylabel('walk')
    plt.title('random walk test')
    plt.axhline(y = 0, color = 'r', linestyle = 'dotted')
    plt.show()
    return

# TEST
#------------------------------------------------

# generate a sequence of n random bits
n = 1000
random_seq = f'{random.getrandbits(n):=0{n}b}'
random_walk(random_seq)

