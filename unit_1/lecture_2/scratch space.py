# -*- coding: utf-8 -*-
"""Practice code written during lecture 2.

Created on Tue Jan  5 16:16:58 2021

@author: nathan.m
"""

testlist = ['a', 'b', 'c']
print(testlist[1:])

x = 13
y = 8
x >> y

for i in range(8):
    print(i)
    
0 % 2

(0 >> 0) % 2 == 1

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        print('iteration ', i, 'beginning')
        combo = []
        for j in range(N):
            # test bit jth of integer i
            print('iteration', j, 'beginning')
            print('i >> j is ', i >> j)
            print('divided by 2 is ', ((i >> j) % 2))
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
items = ['A','B','C']

N = len(items)
# enumerate the 2**N possible combinations
for i in range(2**N): # 0, 1, 2 ...
    print()
    print('i iteration ', i, 'beginning') # interation begins
    print()
    combo = []
    for j in range(N): # range over the LENGTH
        # test bit jth of integer i
        print('j iteration', j, 'beginning')
        print('i >> j is ', i >> j)
        print('divided by 2 is ', ((i >> j) % 2))
        if (i >> j) % 2 == 1: # shift the bits by length. whole number check
            combo.append(items[j]) # append the item found at this bit
            print('APPEND triggered. Item appended: ', items[j])
        print('(j)TERATION ', j, 'ending... combo result of ', combo)
    print('(i)TERATION ', i, ' ending... loop yield is ', combo)
    print()
for i in range(3**N):
    print()
    print('i iteration ', i, 'beginning')
    print()
    combo = []
    for j in range(N):
        # test bit jth of integer i
        print('j iteration', j, 'beginning')
        print('i >> j is ', i >> j)
        print('divided by 2 is ', ((i >> j) % 2))
        if (i >> j) % 2 == 1:
            combo.append(items[j])
        print('j iteration ', j, 'ending with combo result of ', combo)
    print(combo)
    
# a recursive call to place a single item into all 3 bags, yielding each time
items = ['A','B','C']

ground = []
bag1 = []
bag2 = []
combo = (ground, bag1, bag2)
def rplace(items, ground, bag1, bag2, combo):
    itemhotseat = items
    combohotseat = combo
    for i in range(len(items))
        itemhotseat = items[i]    
        
        for t in range(2):
            combohotseat[t].append(itemhotseat[0]) # place it
                
            else len(items) >= 1:
            
            del(items[0]) # remove the target item, it has been placed
        yield (combohotseat[1], combohotseat[2])

# a recursive call to place a single item into all 3 bags, yielding each time
items = ['A', 'B','C']
ground = []
bag1 = []
bag2 = []
combo = (ground, bag1, bag2)
def rplacesingle(items):
    for p in range(2):
        combo[p].append(items[0]) # place it
        del(items[0]) # remove the target item, it has been placed
        if len(items) >= 1:
            
        yield (bag1, bag2)