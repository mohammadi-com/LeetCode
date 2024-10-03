import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    num_positives = num_negatives = num_zeros = 0
    len_arr = len(arr)
    for i, j in enumerate(arr):
        if j > 0:
            num_positives += 1
        elif j < 0:
            num_negatives += 1
        else:
            num_zeros += 1
    print("{:.6f}\n".format(num_positives/len_arr)+
          "{:.6f}\n".format(num_negatives/len_arr)+
          "{:.6f}".format(num_zeros/len_arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    print(arr)

    plusMinus(arr)