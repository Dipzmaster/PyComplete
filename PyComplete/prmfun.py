# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:52:25 2021

@author: HP
"""

from math import sqrt
"""
Determines the primality of a given value.
n an integer to test for primality.
Returns true if n is prime; otherwise, returns false.
"""
def is_prime(n):
    root = round(sqrt(n)) + 1
# Try all potential factors from 2 to the square root of n
    for trial_factor in range(2, root):
        if n % trial_factor == 0: # Is it a factor?
            return False # Found a factor
    return True # No factors found
"""
Tests for primality each integer from 2 up to a value provided by the user.
If an integer is prime, it prints it; otherwise, the number is not printed.
"""
def main():
    max_value = int(input("Display primes up to what value? "))
    for value in range(2, max_value + 1):
        if is_prime(value): # See if value is prime
            print(value, end=" ") # Display the prime number
    print() # Move cursor down to next line
main() # Run the program
