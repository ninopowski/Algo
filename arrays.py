import numpy as np
# Majority element of an array is defined as a value x for which
# strictly more than half of array elements
# are equal to x. Output the majority element of the given array a,
# or -1 if the array doesn't have majority element.
#
# The first line of the input contains an integer N - the number of elements in the array. 1 <= N <= 100.
# The second line of the input contains N integers - the elements of the array,
# separated with single spaces. 1 <= ai <= 100.
#
# Example
# input
# 5
# 8 8 2 4 8
# output
# 8
# input
# 3
# 1 2 3
# output
# -1

N = 7
ai = [1, 1, 2, 3, 1, 2, 1, 3, 1]
ap = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12]


def for_list(N, l):
    dominant = None
    for i in l:
        if l.count(i) > N/2:
            dominant = i
    if dominant:
        print(dominant)
    else:
        print(-1)


for_list(N, ap)


M = 9
ay = np.array(ai)

def for_array(N, l):
    dominant = None
    for i in l:
        if np.count_nonzero(l==i) > N/2:
            dominant = i
    if dominant:
        print(dominant)
    else:
        print(-1)

for_array(M, ay)
print('something')