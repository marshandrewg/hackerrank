#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    highestSum = hourglassHelper(0, 0, arr)
    for r in range(4):
        for c in range(4):
            sum = hourglassHelper(r, c, arr)
            if sum > highestSum:
                highestSum = sum
    return highestSum
def hourglassHelper(r, c, arr):
    sum = 0
    if r > 3 or c > 3:
        return 0
    for offset in range(3):
        sum += arr[r][c + offset]
        sum += arr[r + 2][c + offset]
    sum += arr[r + 1][c + 1]
    return sum
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
    print()
    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
