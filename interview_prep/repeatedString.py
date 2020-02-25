#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    aTotal = 0
    aPerS = s.count('a')
    length = len(s)
    # Number of complete strings, partials uncounted
    wholeSRepeats = math.floor(n/length)
    wholeSRepeatsA = wholeSRepeats * aPerS

    partialLength = (n % length)
    partial = s[0:partialLength]
    aPerPartial = partial.count("a")

    aTotal = wholeSRepeatsA + aPerPartial
    return aTotal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
