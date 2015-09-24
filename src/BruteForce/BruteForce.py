#!/usr/bin/env python

import math

def square_dist(point, query_point):
    return (point[0]-query_point[0])**2 + (point[1]-query_point[1])**2 + (point[2]-query_point[2])**2

class BruteForce():
    def __init__(self, data, h):
        self.data = data
        self.h = h

    def nearest_neighbours(self, query_point, radius=None):
        if radius is None:
            radius = self.h
        nn = []
        for point in self.data:
            if square_dist(point, query_point) < radius**2:
                nn.append(point)
        return nn
