# -*- coding: utf-8 -*-
"""
Problem set 1 covering lectures 1-3.

A three part problem set involving the transport of items via competing
optimization models.

Part 1: a greedy algorithm
Part 2: a brute force algorithm
Part 3: algorithm comparison

Created on Sat Jan 30 20:29:33 2021

@author: nathan.m
"""


def greedy_cow_transport(input_dict, cargo_limit):
    """
    Optimizes a multi-part transport operation.

    Parameters
    ----------
    input_dict : dict
        dictionary matching payload item names to weights(in tons).
            example entry/types/max values:
                {unique_payload: 100}
                {str: int}
                {n/a: 0-100}
    cargo_limit : int
        weight limit per transport operation

    Returns
    -------
    list_of_lists : list
        A list of lists. Each inner list represents a round trip transport
        operation. Payloads are identified via unique_payload parameter passed
        in at runtime. Each trip orders heavier payloads first but order of
        trips is arbitrary.
            example:
                list_of_lists = [[pl1, pl2], [pl3, pl4]]
    """
d = {}
