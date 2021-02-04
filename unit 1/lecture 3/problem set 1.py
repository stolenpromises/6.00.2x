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

# part 1 BEGIN


# python 3.6.2+
def greedy_cow_transport_modern(input_dict, cargo_limit):
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
    cargo_history : list
        A list of lists. Each inner list represents a round trip transport
        operation. Payloads are identified via unique_payload parameter passed
        in at runtime. Each trip orders heavier payloads first. Arbitrary
        tiebreak and trip order.
            example:
                cargo_history = [[pl1, pl2], [pl3, pl4]]
    """
    # helper function to allow for sorting the dictionary by value
    def valuetarget(x):
        """Return dictionary item values."""
        return x[1]

    # convert the input dictionary into a dictionary sorted by weight
    sorted_dict = {key: value for (key, value) in sorted(input_dict.items(), key=valuetarget, reverse=True)}
    cargo_history = []  # initiate the list of lists
    # run a takeoff loop as long as there is remaining payload
    while sorted_dict != {}:
        # plane landed empty
        cargo = []
        cargo_weight = cargo_limit
        # load payload biggest to smallest and don't exceed the cargo limit
        for i in sorted_dict:  # loop over remaining payload
            if sorted_dict[i] <= cargo_weight:  # cargo room for payload
                cargo.append(i)  # add the payload to cargo
                cargo_weight -= sorted_dict[i]  # add the payload weight
        for i in cargo:  # remove loaded payload
            del(sorted_dict[str(i)])  # payload accounted for... remove
        cargo_history.append(cargo)  # record the delivery
    return cargo_history


# python 3.5
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
    cargo_history : list
        A list of lists. Each inner list represents a round trip transport
        operation. Payloads are identified via unique_payload parameter passed
        in at runtime. Each trip orders heavier payloads first. Arbitrary
        tiebreak and trip order.
            example:
                cargo_history = [[pl1, pl2], [pl3, pl4]]
    """
    # helper function to allow for sorting the dictionary by value
    def valuetarget(x):
        """Return dictionary item values."""
        return x[1]

    # convert the input dictionary into a list of lists sorted by weight
    lolsorted = []
    lolsorted = [[k, v] for (k, v) in sorted(input_dict.items(), key=valuetarget, reverse=True)]
    cargo_history = []  # initiate the list of lists
    # run a takeoff loop as long as there is remaining payload
    while lolsorted != []:
        # plane landed empty
        purgelist = []
        cargo = []
        cargo_weight = cargo_limit
        # load payload biggest to smallest and don't exceed the cargo limit
        for i in range(len(lolsorted)):  # loop over remaining payload
            if lolsorted[i][1] <= cargo_weight:  # cargo room for payload
                cargo.append(lolsorted[i][0])  # add the payload to cargo
                cargo_weight -= lolsorted[i][1]  # add the payload weight
                purgelist.append(lolsorted[i])  # append for removal
        for i in purgelist:  # loop over payload which was loaded
            lolsorted.remove(i)  # payload accounted for... remove
        cargo_history.append(cargo)  # record the delivery
    return cargo_history

# sample dictionary for testing
# sample = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
# samplelimit = 10
# print(greedy_cow_transport(sample, samplelimit))

#temp
# cargo_weight = 10
# test = ('Callie', 2)
# x = (greedy_cow_transport({'Milkshake': 75, 'Clover': 5, 'Patches': 60, 'Muscles': 65, 'Louis': 45, 'Miss Bella': 15, 'Polaris': 20, 'Lotus': 10, 'Horns': 50, 'MooMoo': 85}, 100))

# x = {'Milkshake': 75, 'Clover': 5, 'Patches': 60, 'Muscles': 65, 'Louis': 45, 'Miss Bella': 15, 'Polaris': 20, 'Lotus': 10, 'Horns': 50, 'MooMoo': 85}
# lolsorted = [[k, v] for (k, v) in sorted(x.items(), key=valuetarget, reverse=True)]
# def valuetarget(x):
#     return x[1]

# part 1 END
# part 2 BEGIN

