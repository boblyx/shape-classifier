"""
Python script to synthesize dataset.
Generate equal no.s of each shape and shuffle.
"""
__author__ = "boblyx"

import sys
import math
from copy import deepcopy
from uuid import uuid4
from random import randrange, uniform
sys.path.append('../')
from geom_utils import vec_utils #.vec_utils import vec2dAngle, pointsTo2DVec

BASE = {"e": [], "p": [], "s": []}
N = 50

def rNum():
    return randrange(-N,N)

def rRad():
    """
    Generates random radians between pi/8 to pi/2
    """
    return uniform(math.pi/8, math.pi/2)

def gPoint():
    """
    Generates a point representation

    """
    d = deepcopy(BASE)
    d["p"] = [[rNum(), rNum()]]
    d["s"] = [0]
    return d

def gLine():
    """
    Generates a line representation

    """
    d = deepcopy(BASE)
    d["e"] = [[0,1]]
    d["p"] = [[rNum(), rNum()], [rNum(), rNum()]]
    d["s"] = [1]
    return d

def gTri():
    """
    Generates a Triangle representation
    - Generate a line first
    - Get angle relative to Y axis.
    - Generate a random number offset to add to the angle to create a new line
    - Generate a random distance 
    - Get point on the new line from the distance obtained in previous step.

    """
    l = [[rNum(), rNum()], [rNum(), rNum()]]
    v1 = vec_utils.pointsTo2DVec(l[0], l[1])
    v2 = [0, 1]
    r = rRad() + vec_utils.vec2dAngle(v1,v2)
    p3 = vec_utils.rotatePointByPivot(l[0], l[1], r)

    d = deepcopy(BASE)
    d["e"] = [[0,1],[1,2],[2,0]]
    d["p"] = [l[0], l[1], p3]
    d["s"] = [2]
    return d

def gSquare():
    """
    Generates a square representation of random orientation.
    - Generate a line first (point A, B)
    - Rotate startpoint by 270 deg using end as pivot(point D)
    - Rotate endpoint by 90 deg using start as pivot(point C) 
    """
    A = [rNum(), rNum()]
    B = [rNum(), rNum()]
    C = vec_utils.rotatePointByPivot(A, B, math.pi/2)
    D = vec_utils.rotatePointByPivot(B, A, 3*math.pi/2)

    d = deepcopy(BASE)
    d["e"] = [[0,1],[1,2],[2,3],[3,0]] # May jumble up start index,but similar order
    d["p"] = [A, B, C, D]
    d["s"] = [3]
    return d

if __name__ == "__main__":
    gTri();
