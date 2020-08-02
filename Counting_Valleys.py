#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    L=0
    V=0
    for i in s:
        if i == 'U':
            L += 1
            if L == 0:
                V += 1
        else:
            L -= 1
        
    return V

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = str(input())

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
