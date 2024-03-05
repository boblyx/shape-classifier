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
sys.path.append('./packages')
from geom_utils.vec_utils import vec2dAngle, pointsTo2DVec

BASE = {"e": [], "p": [], "s": []}

def rNum():
    return randrange(-300,300)

def rRad():
    """
    Generates random radians between -pi to pi
    """
    return uniform(-math.pi, math.pi)

def rotate(shape_verts, angle = 0):
    """
    Rotates a sequence of vertices by given angle in radians.
    :param shape_verts: List of shape vertices.
    :param angle: Angle to rotate in radians.
    """

    pass

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
    v1 = pointsTo2DVec(l[0], l[1])
    v2 = [0, 1]
    r = rRad() + vec2dAngle(v1,v2)
    print(vec2dAngle(v1, v2))
    print(r)
    pass

def gSquare():
    """
    Generates a square representation of random orientation.
    """
    pass

gTri();
