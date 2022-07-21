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

# visualize a random string as a matrix
#--------------------------------------------
def matrix_visualization(rnd_seq):

    # reduce to a square matrix
    size = int(math.sqrt(len(rnd_seq)))
    rnd_seq = rnd_seq[0:size*size]

    x = np.array(list(rnd_seq.replace('0','b').replace('1','r')))
    shape = ( size, size )
    mat  = x.reshape( shape )
    X,Y = np.meshgrid(np.arange(mat.shape[1]), np.arange(mat.shape[0]))

    # plot
    plt.scatter(X.flatten(), Y.flatten(), c=mat.flatten())
    plt.title("matrix visualisation")
    plt.show()
    return

# TEST
#------------------------------------------------
# generate a sequence of n random bits
n = 1000
random_seq = f'{random.getrandbits(n):=0{n}b}'
matrix_visualization(random_seq)

