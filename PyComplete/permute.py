# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 20:29:54 2021

@author: HP
"""

# The first letter varies from A to C
for first in 'ABC':
    for second in 'ABC': # The second varies from A to C
        if second != first: # No duplicate letters allowed
            for third in 'ABC': # The third varies from A to C
# Don't duplicate first or second letter
                if third != first and third != second:
                    print(first + second + third)