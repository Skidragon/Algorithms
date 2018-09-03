#!/usr/bin/python

import sys

def climbing_stairs(n):
  n += 1
  def fib(n):
    if n <= 2:
      if n <= 0:
        return 0
      else:
        return 1
    
    return (fib(n - 1) +
    fib(n - 2) + 
    fib(n - 3))
  
  return fib(n)

if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python climbing_stairs.py [n]` with different n values
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')