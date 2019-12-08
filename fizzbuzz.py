#!/usr/bin/env python3
"""FizzBuzz"""

for x in range(1,101):
    fizz = 'fizz' if not x % 3 else ''
    buzz = 'buzz' if not x % 5 else ''
    
    if fizz or buzz:
        print(fizz+buzz)
    else:
        print(x)
