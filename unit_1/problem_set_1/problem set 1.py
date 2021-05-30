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
import ps1_partition  # returns a helper generator used in part 2
import time  # required for part 3

# PART 1 BEGIN


# python 3.6.2+
def greedy_cow_transport_modern(input_dict, cargo_limit):
    """
    Return a multi-part transport operation configuration via a
    greedy algorithm implementation which may or may not be optimal.

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
    sorted_dict = {key: value for (key, value) in sorted(input_dict.items(),
                                                         key=valuetarget,
                                                         reverse=True)}
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
    Return a multi-part transport operation configuration via a
    greedy algorithm implementation which may or may not be optimal.

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
    lolsorted = [[k, v] for (k, v) in sorted(input_dict.items(),
                                             key=valuetarget, reverse=True)]
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


# sample dictionary for testing part 1
print('part 1 answer is ', greedy_cow_transport({"Jesse": 6, "Maybel": 3,
                                                 "Callie": 2, "Maggie": 5},
                                                10))
print()

# PART 1 END


# PART 2 BEGIN


def brute_force_cow_transport(input_dict, cargo_limit):
    """
    Return a multi-part transport operation configuration via a brute
    force algorithm implementation which will be optimal with respect to
    minimizing total trips.

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
    payloadlist = list(input_dict)  # convert input dict into a list
    # loop over the helper generator till a set within the limits is found
    champion = None  # iniate a winner variable
    for pset in ps1_partition.get_partitions(payloadlist):  # loop partitions
        cargochecks = []  # initiate a cargo checklist
        for cargoload in pset:  # loop each cargo load within the partition
            cargototal = 0  # prepare to add payloads
            for pl in cargoload:  # loop payloads within the cargo load
                cargototal += input_dict[pl]  # lookup and sum payload weights
            if cargototal <= cargo_limit:  # cargo is within limit
                cargochecks += 'p'
            else:  # cargo exceeds limit
                cargochecks += 'f'
        if 'f' not in cargochecks:  # check for cargo_limit violations
            if champion is None:  # check if we have a champion already
                champion = pset  # no winner, assign new champion
            elif len(pset) < len(champion):  # check length vs champion
                champion = pset  # new champion found
    return champion  # output the last used partition


# sample dictionary for testing part 2
print('part 2 answer is ', brute_force_cow_transport({'Horns': 25, 'Lotus': 40,
      'Miss Bella': 25, 'Boo': 20, 'Milkshake': 40, 'MooMoo': 50}, 100))
print()

# PART 2 END


# PART 3 BEGIN


def compare_cow_transport_algorithms(input_dict, cargo_limit, function_list):
    """
    Compare the running time of greedy vs brute force algorithms in part 1/2.

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
    function_list : list
        list of functions which will be timed as they run on the above two
        parameters

    Returns
    -------
    function : print statement
        print statement identifying each function which was timed
    time : print statement
        print statement indicating running time in seconds
    """
    # time the greedy algorithm
    def algorithm_time(f, input_dict, cargo_limit):
        """Print the running time of called function."""
        start = time.time()  # start the clock on the below code
        f(input_dict, cargo_limit)
        end = time.time()  # end the clock
        print('function: ', f)  # print the function name
        print('running time ', end - start)
    # loop over functions in the list
    for f in function_list:
        algorithm_time(f, input_dict, cargo_limit)  # pass function for timing


# parse the sample text document into a dictionary
ps1_dict = {}
with open('ps1_cow_data.txt') as f:  # open dataset
    for line in f:  # iterate over each line
        line = line.strip()  # strip it of linebreaks and whitespace
        key = ''  # initiate a key to be appended to
        value = 0  # initiate a value to be appended to
        for i in range(len(line)):  # loop over an index of the line
            if line[i] != ',':  # as long as we havn't reached the comma
                key += line[i]  # append the letter to the key
            elif line[i] == ',':  # we have reached the comma
                value = int(line[i+1:len(line)])  # assign the value
                break  # stop iterating
        ps1_dict[key] = value  # add the entry to the dictionary

# build the function list
function_list = []
function_list.append(greedy_cow_transport)
function_list.append(brute_force_cow_transport)

# print results
print('part 3')  # note the beginning of part 3 components
print()
print('dictionary:')
print(ps1_dict)  # print the newly parsed dictionary
print()
print('function list:')
print(function_list)
print()
print('running times:')
compare_cow_transport_algorithms(ps1_dict, 10, function_list)

# PART 3 end
