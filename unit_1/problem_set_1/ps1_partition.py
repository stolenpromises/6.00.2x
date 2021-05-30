# -*- coding: utf-8 -*-
"""
A pair of helper functions provided with problem set 1 that generates all the
set partitions for a set of payloads.

Created on Thu Feb  4 08:48:54 2021

@author: MITx-6.00.2x
"""

# From codereview.stackexchange.com
def partitions(set_):
    """Take as input a set and generates partitions.

    Parameters
    ----------
    set_ : list

    Returns
    -------
    A list of partitions.
    """
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


#  This is a helper function that will fetch all of the available
#  partitions for you to use for your brute force algorithm.

def get_partitions(set_):
    """Take as input a list and returns a generator.

    Parameters
    ----------
    set_ : list

    Returns
    -------
    A generator that contains all the possible partitions of this list,
    from 0-partitions to n-partitions, where n is the length of this list.
    """
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

### Uncomment the following code  and run this file
### to see what get_partitions does if you want to visualize it:

# for item in (get_partitions(['a','b','c','d'])):
#     print(item)