#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    res = 0
    lst = []
    for i in path:
        if i == "D" and (len(lst)==0):
            lst.append("D")
        elif i == "D" and (len(lst)!=0):
            if lst[-1] == "D":
                lst.append("D")
            elif lst[-1] == "U":
                lst.pop()
        elif i == "U" and (len(lst)==0):
            lst.append("U")
        elif i == "U" and (len(lst)!=0):
            if lst[-1] == "U":
                lst.append("U")
            elif lst[-1] == "D":
                lst.pop()
                if len(lst) == 0:
                    res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
