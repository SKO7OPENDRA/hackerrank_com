# Read an integer N.
# # Without using any string methods, try to print the following:
# 123...N
#
# Input Format
# The first line contains an integer .
# Output Format
# Output the answer as explained in the task.
N = int(input())
for i in range(N):
    print(i+1, end="")