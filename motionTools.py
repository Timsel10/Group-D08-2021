import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
from scipy.interpolate import interp1d
import sync

def forced_mass_spring_damper(t, y, c, k, x_forced, v_forced):
    """
    Inputs:
    t is a float for time
    y is a list [x, x']
    c is a float which is infact c/m
    k is a float which is infact k/m
    x_forced is an interp1d function which returns a x_forced value for a given t within the domain
    v_forced is an interp1d function which returns a v_forced value for a given t within the domain

    Output:
    dydt is a list [x'', x']

    Description:
    This is the function required by the solve
    """
    raise NotImplementedError
    # commented below is some old code which can be deleted in the final version
    #x_forced = np.exp(-((t - 1) ** 2))
    #v_forced = -2 * (t - 1) * np.exp(-((t - 1) ** 2))
    x, x_prime = y
    dydt = [x_prime, -c * x_prime - k * x + x_forced(t) * k + v_forced(t) * c]
    return dydt


class headMotion:
    def __init__(self, simMotionArray, headMotionArray, filename):
        """
        Inputs:
        simMotionArray is a numpy array
        headMotionFile is a string which is the path to the headMotionFile

        simMotion path isn't needed to reduce the number of times that file is loaded
        """
        simMotion = simMotionArray
        headMotion = headMotionArary
        headMotion.sync_head_motion()
        simMotion.transform()
        headMotion.transform()

    def transform(self):
        # to be copied from transform.py or imported and run from there
        raise NotImplementedError


class singleDOFsystem:
    def __init__(self, simMotion, headMotion):
        #initialConditions = 
        raise NotImplementedError    

    def interpolate(self):
        """
        Inputs:
        Interpolating 
        """
        raise NotImplementedError
        return interp1d(...)

    def solveODE(self):
        raise NotImplementedError
        return solve_ivp(forced_mass_spring_damper, self.initialConditions, )




