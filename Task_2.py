# Print the cli arguments list python test.py arg1 arg2 arg3

Solution 1:

import sys

for x in range(1, len(sys.argv)):
  print(sys.argv[x])


Solution 2:

import sys
print(sys.argv[1: ])






