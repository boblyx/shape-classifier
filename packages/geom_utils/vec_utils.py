from copy import deepcopy
import math
import numpy as np

def vec2dAngle(v1, v2):
    """
    :param v1: Vector 1
    :param v2: Vector 2
    :return: Angle between the two vectors.

    """
    return math.atan2(
            v1[1] * v2[0] - v1[0] * v2[1],
            v1[0] * v2[0] + v1[1] * v2[1]
            )

def pointsTo2DVec(s, t):
    """
    :param s: Source
    :param t: Target
    :return: Vector as a 2D array

    """
    return([t[0] - s[0], t[1] - s[1]])

def rotatePointByPivot(pivot = [0, 0], target = [0, 1], angle = math.pi/2):
    """
    :param pivot: Pivot around which point is to be rotated
    :param target: Target point to rotate
    :param angle: Rotatation angle in radians.
    :return: New point that is rotated.

    """

    sa = math.sin(angle)
    ca = math.cos(angle)

    tc = deepcopy(target)
    tc[0] -= pivot[0]
    tc[1] -= pivot[1]

    x = tc[0] * ca - tc[1] * sa
    y = tc[0] * sa + tc[1] * ca

    return [x + pivot[0], y + pivot [1]]
