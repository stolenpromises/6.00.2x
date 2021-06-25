# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 09:56:21 2021

@author: nathan.m
"""


def max_contig_sum(L):
    """Return the maximum sum of a contiguous subsequence in L.

    L, a list of integers, at least one positive.
    """
    # build a power set
    list_of_lists = []
    for e1 in range(len(L)):  # iterate over the lists index positions
        sendlist = []  # intiate a list to send
        sendlist.append(L[e1])  # append the starting element
        list_of_lists.append(tuple(sendlist))  # append the sendlist
        for e_next in L[(e1+1):len(L)]:  # iterate over all remaining elements
            sendlist.append(e_next)  # append the next element
            list_of_lists.append(tuple(sendlist))  # append the sendlist

    # computer all subsets, find the maximum contiguous sequence
    champion = 0
    for subset in list_of_lists:  # iterate of the list of lists
        contendor = 0
        for e in subset:  # iterate over the tuple
            contendor += e  # sum up the elements
        if contendor > champion:  # a new champion has immerged
            champion = int(contendor)  # give him his crown
    return champion  # send him to the people


L = [3, 4, -1, 5, -4]
print(max_contig_sum(L))
