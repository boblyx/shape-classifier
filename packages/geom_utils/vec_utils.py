import math
import numpy as np

def vec2dAngle(v1, v2):
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
