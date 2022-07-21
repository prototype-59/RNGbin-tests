#!/usr/bin/python
#----------------------------------------------------------------------------
# Created By  : Aleksandar Radovanovic
# Created Date: 2022-07-21
# version ='1.0'
# ---------------------------------------------------------------------------

import math
import random
from string import digits
import numpy as np
import matplotlib.pyplot as plt

#  Shows and returns relative frequency
#   of digits 0 and 1
#------------------------------------------------

def digits_frequency(rnd_seq):
    count_0 = 0
    count_1 = 0
    for digit in rnd_seq:
        if digit == '0':
            count_0 += 1
        else:
            count_1 += 1
    rf_0 = count_0 / len(rnd_seq)
    rf_1 = count_1 / len(rnd_seq)
    
    # plot
    digitsfrequency = [rf_0,rf_1]
    digits = ["0", "1"]
    plt.xlabel("digits")
    plt.ylabel("frequency")
    plt.title("relative frequency of digits")
    plt.bar(digits, digitsfrequency, color=['b','r'])
    for i in range(len(digits)):
        plt.text(i, digitsfrequency[i]/2,'{:,.3f}'.format(digitsfrequency[i]), ha = 'center')
    plt.show()

    # return the relative frequency of digits
    return[rf_0,rf_1]

# TEST
#------------------------------------------------
# generate a sequence of n random bits
n = 1000
random_seq = f'{random.getrandbits(n):=0{n}b}'
digits_frequency(random_seq)

