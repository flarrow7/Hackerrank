#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump=0
    i=0
    c.append('x')
    n=len(c)-2

    while i < n:
        if (c[i+2] ==1 and c[i+1]==0):
            jump+=1
            i+=1
        else:
            jump+=1
            i+=2
    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
