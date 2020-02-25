# Read an integer N. For all non-negative integers i < N, print i**2 . See the sample for details.
#
# Input Format
# The first and only line contains the integer, N.
# Constraints
# 1 <= N <= 20
# Output Format
# Print  lines, one corresponding to each .

N = int(input())
i = 0

while i < N:
    n = i**2
    i += 1
    print (n)