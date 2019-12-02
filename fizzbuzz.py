#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FizzBuzz

Paul Egeler
2019/12/01

Print 1:100

Except
-------------------------------
For multiples of 3, write Fizz
For multiples of 5, write Buzz
For multiples of 3 and 5, write FizzBuzz
"""

for x in range(1,101):
    fizz = 'fizz' if not x % 3 else ''
    buzz = 'buzz' if not x % 5 else ''
    
    if fizz or buzz:
        print(fizz+buzz)
    else:
        print(x)
