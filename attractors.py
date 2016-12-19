#!python2.7

"""
Nick Pleatsikas - Differential Equations
Strange Attractors Project
"""

# External Libraries:
import csv
import numpy as np

# Internal Libraries:
from render import *

"""
Attractor Super Class:
Desc: This class provides general functions for strange attractors.
- euler_method: Euler's Method to generate sets of points.
- export_csv: Exports coordinates to csv file.
- render_3d: Renders the graph of the attractor.
"""
class Attractor(object):
    # Initializes class with three arrays of size 10001.
    def __init__(self, step, nsteps):
        # User supplied values.
        self.step = step
        self.nsteps = nsteps
        
        self.x_values = np.zeros(nsteps + 1)
        self.y_values = np.zeros(nsteps + 1)
        self.z_values = np.zeros(nsteps + 1)
        
    # euler_method : function -> list list list
    # Performs Euler's Method n times with a certain step size, number of
    # steps, and a given attractor function.
    def euler_method(self, attractor_name):
        for i in range(self.nsteps):
            x_prime, y_prime, z_prime = attractor_name(self.x_values[i], 
                                                         self.y_values[i], 
                                                         self.z_values[i])
            self.x_values[i + 1] = self.x_values[i] + (x_prime * self.step)
            self.y_values[i + 1] = self.y_values[i] + (y_prime * self.step)
            self.z_values[i + 1] = self.z_values[i] + (z_prime * self.step)
               
    # export_csv : string -> file
    # Exports CSV with computed values.
    def export_csv(self, fname = 'exports.csv'):
         rows = zip(self.x_values, self.y_values, self.z_values)
         # File writer:
         with open(fname, 'wb') as f:
             writer = csv.writer(f)
             for row in rows:
                 writer.writerow(row)
               
    # render_3d : -> window
    # Calls render.py to render a 3D plot through matplotlib.
    def render_3d(self):
         render(self.x_values, self.y_values, self.z_values)

"""
Rossler Attractor Class:
Desc: Provides Rossler function.
- rossler: Rossler attractor function.
"""
class RosslerAttractor(Attractor):
    # Initializes class with three coefficients.
    def __init__(self, a, b, c, *args, **kwargs):
        # Allows class methods to be accessed by superclass and inherit init.
        super(RosslerAttractor, self).__init__(*args, **kwargs)
        # Initial conditions.
        self.a = a
        self.b = b
        self.c = c
    
    # rossler : int int int -> int int int
    # Rossler attractor function. Takes x, y, & z coordinates and returns the 
    # velocity based on that point according to the Rossler system.
    def rossler(self, x, y, z):
        x_prime = (-1*y) - z
        y_prime = x + self.a*y
        z_prime = self.b + z*(x-self.c)
        return x_prime, y_prime, z_prime

"""
Lorenz Attractor Class:
Desc: Provides Lorenz function.
- Lorenz: Lorenz attractor function.
"""
class LorenzAttractor(Attractor):
    def __init__(self, a, b, c, *args, **kwargs):
        # Allows init to be inherited by parent class.
        super(LorenzAttractor, self).__init__(*args, **kwargs)
        # Initial arguments.
        self.a = a
        self.b = b
        self.c = c

    # lorenz : int int int -> int int int
    # Lorenz attractor function. Takes x, y, & z coordinates and returns the 
    # velocity based on that point according to the Lorenz system.
    def lorenz(self, x, y, z):
        x_prime = self.a * (y - x)
        y_prime = x * (self.b - z) - y
        z_prime = x * y - self.c - z
        return x_prime, y_prime, z_prime
