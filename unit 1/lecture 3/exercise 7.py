# -*- coding: utf-8 -*-
"""
An exercise to build a weighted edge class that is a subclass of Edge from
previous exercises. Comment lines indicate exercise supplied vs novel code.

Created on Sat Jan 30 03:55:45 2021

@author: nathan.m
"""

#Exercise supplied code begin
class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
#Exercise supplied code end

class WeightedEdge(Edge):
    """
    A subclass of Edge() which adds a weight parameter, an associated get
    method and a node-to-node weight summation method.
    """
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() + ' (' + str(self.weight) + ')'