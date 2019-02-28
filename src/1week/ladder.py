import sys

i = int(sys.argv[1])
for j in range(i):
    print(" " * (i-j-1) + "#"*(j+1))
