from numba import njit
import numpy as np
import glm
import math

# resolution
WIN_RES = glm.vec2(1600, 900)

# colors
BG_COLOR = glm.vec3(.1, .16, .25)
