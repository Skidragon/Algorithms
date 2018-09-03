#!/usr/bin/python

import sys

def climbing_stairs(n, ranOnce = False):
    if ranOnce == False:
      n += 1
      ranOnce = True

    if n <= 2:
      if n <= 0:
        return 0
      else:
        return 1
      
    return (climbing_stairs(n - 1, ranOnce) + 
    climbing_stairs(n - 2, ranOnce) + 
    climbing_stairs(n - 3, ranOnce))

if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python climbing_stairs.py [n]` with different n values
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')