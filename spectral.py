#!/usr/bin/python
#----------------------------------------------------------------------------
# Created By  : Aleksandar Radovanovic
# Credit      :  Steven Kho Ang  
#             : https://github.com/stevenang/randomness_testsuite/blob/master/Spectral.py
# Created Date: 2022-07-21
# version ='1.0'
# ---------------------------------------------------------------------------

import math
import random
from string import digits
import numpy as np
import matplotlib.pyplot as plt

import scipy.special as spc
import scipy.fftpack as sff

# spectral test (for sequence length > 1000)
# The purpose of this test is to detect periodic features 
# (i.e., repetitive patterns that are near each other)
# in the tested sequence that would indicate a deviation 
# from the assumption of randomness. The intention is 
# to detect whether the number of peaks exceeding the 95% 
# threshold is significantly different than 5%
#------------------------------------------------
def spectral(rnd_seq, plot = True):
    n = len(rnd_seq)

    # convert (0,1) to (-1, +1)
    up_down = []
    for digit in rnd_seq:
        up_down.append(2 * int(digit) - 1)
    
    # apply a Discrete Fourier Transform (DFT)
    spectral = sff.fft(up_down)

    # modulus gives a sequence of peak heights.
    slice = int(n/2)  #floor(length_of_binary_data / 2)
    modulus = abs(spectral[0:slice])

    # under an assumption of randomness, 95%
    # of the values obtained from the test 
    # should not exceed the 95 % peak height.
    tau = np.sqrt(np.log(1 / 0.05) * n)

    # n0 is the expected theoretical (95%) number of peaks
    n0 = 0.95 * (n / 2) 

    # n1 = observed number of peaks that are less than 5%.
    n1 = len(np.where(modulus < tau)[0])
    d = (n1 - n0) / np.sqrt(n * (0.95) * (0.05) / 4)

    # compute p-value
    pval = spc.erfc(abs(d)/np.sqrt(2))

    # plot (-1, +1) sequence
    if plot:
        x = np.arange(0,n)
        for i in range( len(up_down) ):
            if up_down[i] == -1:
                plt.vlines(x = i, ymin = -1, ymax = 0, color = 'b')  
            else:
                plt.vlines(x = i, ymin = 0, ymax = 1, color = 'r')  

        plt.xlabel('bits')
        plt.ylabel('value')
        plt.yticks([-1,0,1])
        plt.title('spectral test, p-value = ' + str(pval))
        plt.axhline(y = 0, color = 'r', linestyle = 'dotted')
        plt.show()
    
    return pval

# TEST
#------------------------------------------------
# generate a sequence of n random bits
n = 1000
random_seq = f'{random.getrandbits(n):=0{n}b}'
pval = spectral(random_seq)
print(pval)

