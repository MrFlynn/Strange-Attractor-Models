#!python2.7

"""
Nick Pleatsikas - Differential Equations
Strange Attractors Project

Description:

"""

# External Libraries:
import csv
import numpy as np

# Internal Libraries:
from render import *

# Intialize Arrays:
x_init = np.empty((num_steps + 1,))
y_init = np.empty((num_steps + 1,))
z_init = np.empty((num_steps + 1,))
     
x_init[0], y_init[0], z_init[0] = (0., 0., 0.) # Set first position in arrays to 0.

"""
Atractor Super Class:
Desc: This class provides general functions for strange attractors.
- euler_method: Euler's Method to generate sets of points.
- export_csv: Exports coordinates to csv file.
- render_3d: Renders the graph of the attractor.
"""
class Attractor(object):
    # Initializes class with three arrays of size 10001.
    def __init__(self, step, nsteps):
        self.x_values = x_init
        self.y_values = y_init
        self.z_values = z_init
        
        # User supplied values.
        self.step = step
        self.nsteps = nsteps
     
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
    def export_csv(self, fname):
         rows = zip(self.x_values, self.y_values, self.z_values)
         # Check if file name exists. If not, set it to default.
         if not '':
             fname = 'exports.csv'
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
- rossler: rossler attractor function.
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
    # Rossler attractor function.
    def rossler(self, x, y, z):
        x_prime = (-1*y) - z
        y_prime = x + self.a*y
        z_prime = self.b + z*(x-self.c)
        return x_prime, y_prime, z_prime
