#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.

"""
def sockMerchant(n, ar):
    ar.sort()
    new_ar = list(set(ar))
    pair = 0
    for i in range(0, len(new_ar)):
        count=0
        for j in range(0, len(ar)):
            if (new_ar[i] == ar[j]):
                count = count+1
        count = count//2
        pair = pair+count
    return pair

"""
def sockMerchant(n, ar):
    ar.sort()
    ar.append('x')
    count=0
    i=0
    while i <n:
        if ar[i] == ar[i+1]:
            i+=2
            count+=1
        else:
            i+=1    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
