#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    d = dict()
    for letter in s1:
        if letter not in d.keys():
            d[letter] = "s1"
    for letter in s2:
        if letter not in d.keys():
            d[letter] = "s2"
        elif d[letter] == "s1":
            d[letter] = "s3"
    
    for k in d:
        if d[k] == "s3":
            return ("YES")
    return ("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
