# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:40:41 2021

@author: nathan.m

I misunderstood the complexity of the question at hand in exercise 5...
Nonetheless, this was good practice.
"""

import statistics
import random

def parse_text(filename):
    """Parse text file input into list.

    Parameters
    ----------
    filename : str
        Path to a heart rate text file to be parsed.

    Returns
    -------
    hr : list
        List of hr values

    """
    hr = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            hr.append(float(line))
    return hr


def check_independence(hr_list, sample_runs, sample_size):
    """Return avg std dev of random samples.

    Parameters
    ----------
    hr_list : list
        a list of heart rate samples
    sample_runs : int
        the number of random samples to generate

    Returns
    -------
    avg_std_dev : float
        the average standard deviation of random samples

    """
    sample_std_devs = []
    for i in range(sample_runs):  # iterate for the number of runs
        # append the standard deviation of a random sample
        sample_std_devs.append(statistics.stdev(random.sample(hr_list, sample_size)))
    return statistics.mean(sample_std_devs)  # return the list mean


hr1 = parse_text('hr1.txt')  # parse the first dataset
hr2 = parse_text('hr2.txt')  # parse the second dataset
print(check_independence(hr1, 50, 250))
print(check_independence(hr2, 50, 250))
