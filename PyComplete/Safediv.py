# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:17:24 2021

@author: HP
"""

# Get the dividend and divisor from the user
dividend = int(input('Enter dividend: '))
divisor = int(input('Enter divisor: '))
# We want to divide only if divisor is not zero; otherwise,
# we will print an error message
if divisor != 0:
    print(dividend/divisor)
else:
    print('Error, cannot divide by zero')