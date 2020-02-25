# Let's learn about list comprehensions!
# You are given three integers X, Y, and Z representing the dimensions of a cuboid along with an integer N.
# You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to N.
# Here, 0<=i<=X, 0<=j<=Y, 0<=k<=Z
#
# Input Format
# Four integers X, Y, Z and N each on four separate lines, respectively.
# Constraints
# Print the list in lexicographic increasing order.


# python
# x = int ( raw_input())
# y = int ( raw_input())
# n = int ( raw_input())
# ar = []
# p = 0
# for i in range ( x + 1 ) :
#     for j in range( y + 1):
#         if i+j != n:
#             ar.append([])
#             ar[p] = [ i , j ]
#             p+=1
#             print ar

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

ar = []
p = 0
for i in range (X+1):
    for j in range (Y+1):
        for k in range (Z+1):
            if i+j+k != N:
                ar.append([])
                ar[p] = [i,j,k]
                p+=1
print (ar)