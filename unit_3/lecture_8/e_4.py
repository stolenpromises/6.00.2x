# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 09:25:30 2021

@author: nathan.m
"""
import random
import statistics


def noReplacementSimulation(numTrials):
    """Return a fraction of positive Monte Carlo simulation results.

    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn.

    Parameters
    ----------
    numTrials : int
        number of trials to run

    Returns
    -------
    float
        the fraction of times 3 balls of the same color were drawn

    """
    same_color = []
    trial_counter = numTrials
    while trial_counter > 0:  # loop until the trial counter reaches 0
        bucket = ['r', 'r', 'r', 'g', 'g', 'g']
        draw_result = []
        for draw in range(3):  # iterate 3 draws
            bucket_draw = random.randint(0, len(bucket) - 1)  # random draw
            ball_draw = bucket[bucket_draw]  # ball drawn
            draw_result.append(ball_draw)  # copy from bucket to draw result
            bucket.remove(ball_draw)  # remove from bucket
        if draw_result == ['r', 'r', 'r']:  # 3 reds were drawn
            same_color.append(1)  # append to the list
        elif draw_result == ['g', 'g', 'g']:  # 3 greens were drawn
            same_color.append(1)  # append to the list
        else:  # neither combo presented
            same_color.append(0)  # append to the list
        trial_counter -= 1  # hit the trial counter
    return statistics.mean(same_color)


print(noReplacementSimulation(1000))
