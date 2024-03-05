import math
import numpy as np

def vec2dAngle(p1, p2):
    return math.atan2(
            p1[1] * p2[0] - p1[0] * p2[1],
            p1[0] * p2[0] + p1[1] * p2[1]
            )

print(vec2dAngle([1,0], [1,1]))
