# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:45:36 2021

@author: HP
"""

# Count to n and print each number
def count_to_n(n):
    for i in range(1, n + 1):
        print(i, end=' ')
    print()
print("Going to count to ten . . .")
count_to_n(10)
print("Going to count to five . . .")
count_to_n(5)