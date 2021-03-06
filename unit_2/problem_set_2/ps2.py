# -*- coding: utf-8 -*-
"""
A problem set designed to practice:

    1. Designing a simulation
    2. Implementing a program that uses classes

Created on Sat May 29 19:53:33 2021

@author: nathan.m
"""

# 6.00.2x Problem Set 2: Simulating robots


import math
import random
import ps2_visualize
import pylab
import abc

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6

# === Provided class Position


class Position(object):
    """A Position represents a location in a two-dimensional room."""

    def __init__(self, x, y):
        """Initialize a position with coordinates (x, y)."""
        self.x = x
        self.y = y

    def getX(self):
        """Return x position."""
        return self.x

    def getY(self):
        """Return y position."""
        return self.y

    def getNewPosition(self, angle, speed):
        """Compute and return a new positon after a move.

        Compute and return the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))  # run
        delta_x = speed * math.sin(math.radians(angle))  # rise
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        """Enable the current position to be printed."""
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# a fix for the online grader's ability to import numpy
#import os
#os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
import abc


# === Problem 1
class RectangularRoom(object):
    """Represents a rectangular region containing clean or dirty tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """Initializee a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        # initialize a blank array dirty tiles(int of 0)
        self.arr = np.zeros((self.width, self.height))

    def __str__(self):
        """Return a print representation for the class."""
        return (str(print(self.arr)))

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned(int of 1).

        Assumes that POS represents a valid position inside this room.

        pos: a Position object
        """
        # round float coordinates down and set tile to int of 1
        self.arr[math.floor(pos.x)][math.floor(pos.y)] = 1

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # round float coordinates down and check the queried tile
        if self.arr[math.floor(m)][math.floor(n)] == 1:
            return True  # it is clean
        else:
            return False  # it is dirty

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        cleantiles = 0  # initiate clean tile counter
        for element in self.arr.flat:  # iterate over all array elements in 1D
            if element == 1:  # clean tile found
                cleantiles += 1  # add to the counter
        return cleantiles

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        random_x = random.uniform(0, self.width)  # assign a random x position
        random_y = random.uniform(0, self.height)  # assign a random y position
        return Position(random_x, random_y)  # return a position object

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if 0 <= pos.x < self.width:  # check x within width
            if 0 <= pos.y < self.height:  # check y within height
                return True  # pos is in the room
        else:
            return False  # pos is outside of the room


# === Problem 2
class Robot(object):
    """Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room, speed):
        """Initialize a Robot with the given speed in the specified room.

        The robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room  # assign the room which was passed in
        self.position = room.getRandomPosition()  # assign random position
        room.cleanTileAtPosition(self.position)  # clean position in room
        self.angle = random.uniform(0, 360)  # assign a direction
        self.speed = speed  # assign speed

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.angle

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.angle = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError  # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """

    def updatePositionAndClean(self):
        """Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # establish a target destination
        destination = self.position.getNewPosition(self.angle, self.speed)
        # check the destination against the room
        if self.room.isPositionInRoom(destination) is True:
            self.setRobotPosition(destination)  # move to the destination
            # position variables for readability and float round for grader
            x = math.floor(destination.getX())
            y = math.floor(destination.getY())
            if self.room.isTileCleaned(x, y) is False:  # check for dirt
                self.room.cleanTileAtPosition(destination)  # clean the tile
        else:  # the destination falls outside the room
            self.angle = random.uniform(0, 360)  # set a new random angle

# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """Return mean time-steps for a robot type.

    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    trial_outcomes = {}  # dict of trial:time_steps
    # loop over each trial
    for trial in range(num_trials):
        room = RectangularRoom(width, height)
        robot_pack = {}  # initiate an empty robot pack
        for num in range(num_robots):  # build pack of robot position objects
            robot_pack[num] = robot_type(room, speed)  # iterative dict add
        time_steps = 0  # time step counter
        # advance the pack till cleaning coverage is reached
        while room.getNumCleanedTiles() < min_coverage*room.getNumTiles():
            time_steps += 1  # add 1 tick to the timer
            for robot in robot_pack:  # loop over the pack
                robot_pack[robot].updatePositionAndClean()  # advance
                # break if cleaning threshold is reached
                if room.getNumCleanedTiles() >= min_coverage*room.getNumTiles():
                    break
        trial_outcomes[trial] = time_steps  # trial complete, append result
    time_step_sum = 0  # initiate a sum
    for trial in trial_outcomes:
        time_step_sum += trial_outcomes[trial]  # append a trial outcome
    return time_step_sum / num_trials  # return the average

# =============================================================================
# Uncomment this line to see how much your simulation takes on average
# print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))
# =============================================================================


# === Problem 5
class RandomWalkRobot(Robot):
    """A RandomWalkRobot is a robot with the "random walk" movement strategy.

    It chooses a new direction at random at the end of each time-step.
    """

    def updatePositionAndClean(self):
        """Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # establish a target destination
        destination = self.position.getNewPosition(self.angle, self.speed)
        # check the destination against the room
        if self.room.isPositionInRoom(destination) is True:
            self.setRobotPosition(destination)  # move to the destination
            # position variables for readability and float round for grader
            x = math.floor(destination.getX())
            y = math.floor(destination.getY())
            if self.room.isTileCleaned(x, y) is False:  # check for dirt
                self.room.cleanTileAtPosition(destination)  # clean the tile
            self.angle = random.uniform(0, 360)  # set a new random angle
        else:  # the destination falls outside the room
            self.angle = random.uniform(0, 360)  # set a new random angle

# =============================================================================
# Uncomment this line to see how much your simulation takes on average
# print(runSimulation(1, 1.0, 10, 10, 0.75, 30, RandomWalkRobot))
# =============================================================================


def showPlot1(title, x_label, y_label):
    """Mean time steps for a pack of 1-10 standard vs random walk robots."""
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def showPlot2(title, x_label, y_label):
    """2 standard vs random walk robots time to clean rooms of various sizes.

    X axis: Room aspect ratio
    Y axis: Mean time steps
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


# =============================================================================
# === Problem 6
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
# showPlot1('Mean time steps for a pack of 1-10 standard vs random walk robots',
#           'Robot pack size', 'Mean time steps')
#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#showPlot2('Mean time steps for a pack of 2 standard vs random walk robots '
#          'in various sized rooms', 'Room aspect ratio', 'mean time steps')
# =============================================================================


# =============================================================================
# = test cases

# == problem 1
# testposition = Position(2.1, 4.9)
# offposition = Position(3.1, 4.1)
# testroom = RectangularRoom(5, 5)
# print('the current test room is: ')
# print(testroom)
# print('initiating tile clean at: ', testposition)
# testroom.cleanTileAtPosition(testposition)
# print('cleaning complete. testroom now looks like this :')
# print(testroom)
# print('beginning tile clean check on the test position')
# print('test position x, y is ', testposition.getX(), testposition.getY())
# print(testroom.isTileCleaned(testposition.x, testposition.y))
# print('beginning tile clean check on the off position')
# print(testroom.isTileCleaned(offposition.x, offposition.y))
# print('test random position object is:')
# print(testroom.getRandomPosition())
# outsideposition = Position(6, 6)
# print('test outsideposition object is:')
# print(outsideposition)
# print('testing if outside position is within testroom:')
# print(testroom.isPositionInRoom(outsideposition))
# print('testing if random positionobject is within testroom:')
# print(testroom.isPositionInRoom(testroom.getRandomPosition()))

# == problem 2
# robot = Robot(RectangularRoom(1, 2), 1.0)
# robot.getRobotPosition()

# =============================================================================
