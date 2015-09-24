#!/usr/bin/env python

import math

def square_dist(point, query_point):
    return (point[0]-query_point[0])**2 + (point[1]-query_point[1])**2 + (point[2]-query_point[2])**2

def neighbour_boxes(i, j, k):
    boxes = []
    for p in [1,0,-1]:
        for q in [1,0,-1]:
            for r in [1,0,-1]:
                if p==0 and q==0 and r==0:
                    continue
                if i+p<0 or j+q<0 or k+r<0:
                    continue
                boxes.append([i+p,j+q,k+r])
    return boxes

class SpatialHash():
    '''
    cell(x,y,z,h) = ([(x-x_min)/h], [(y-y_min)/h], [(z-z_min)/h]) = (i,j,k)
    p1 = 73856093, p2 = 19349663 and p3 = 83492791
    Here assumed (x_min, y_min, z_min) = (0,0,0)
    '''

    def __init__(self, data, h, M, p1=73856093, p2=19349663, p3=83492791, create=True):
        '''
        data is the set of points
        h is the support radius of the smoothing kernel
        M is maximum size of hashtable
        '''
        self.M = M
        self.h = h
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        if create:
            self.hashtable = [[] for x in range(M)]
            for point in data:
                i,j,k = self.cell(h,*point)
                key = self.hash(i,j,k)
                self.add_to_hashtable(key,point)
        else:
            pass

    def cell(self, h, x, y, z):
        return int(math.floor(x/h)),int(math.floor(y/h)),int(math.floor(z/h))

    def hash(self, i, j, k, M=None, p1=None, p2=None, p3=None):
        '''
        hash(i,j,k,[optional: M,p1, p2, p3])
        '''
        if M is None:
            M = self.M
        if p1 is None:
            p1 = self.p1
        if p2 is None:
            p2 = self.p2
        if p3 is None:
            p3 = self.p3
        return (i*p1^j*p2^k*p3)%M

    def add_to_hashtable(self, key, value):
        self.hashtable[key].append(value)
        return

    def nearest_neighbours(self, query_point, radius=None):
        '''
        query_point is a list
        if (i,j,k) is the cell.
        Check all combinations of i+1, j+1, k+1, i-1, j-1, k-1, i, j, k.
        '''
        if radius is None:
            radius = self.h
        i,j,k = self.cell(radius,*query_point)
        nn = self.hashtable[self.hash(i,j,k)]
        #check neighbouring boxes as well
        #find candidates
        candidates = []
        for point in neighbour_boxes(i,j,k):
            candidates+=self.hashtable[self.hash(*point)]
        for point in candidates:
            if square_dist(point,query_point) < radius**2:
                nn.append(point)
        return nn
