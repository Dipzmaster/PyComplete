# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 20:05:55 2021

@author: HP
"""

# Counts up from zero. The user continues the count by entering
# 'Y'. The user discontinues the count by entering 'N'.
count = 0 # The current count
entry = 'Y' # Count to begin with
while entry != 'N' and entry != 'n':
    print(count)
# Print the current value of count

    entry = input('Please enter "Y" to continue or "N" to quit: ')
    if entry == 'Y' or entry == 'y':
        count += 1 # Keep counting
# Check for "bad" entry
    elif entry != 'N' and entry != 'n':
        print('"' + entry + '" is not a valid choice')
# else must be 'N' or 'n'