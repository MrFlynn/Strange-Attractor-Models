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
from Render3D import *

# Step size and number of steps:
step = 0.01
num_steps = 10000

# Intialize Arrays:
x_init = np.empty((num_steps + 1,))
y_init = np.empty((num_steps + 1,))
z_init = np.empty((num_steps + 1,))
     
x_init[0], y_init[0], z_init[0] = (0., 0., 0.) # Set first position in arrays to 0.

"""
Atractor Super Class:
Desc: This class provides general functions for chaotic attractors.
- EulerMethod: Euler's Method to generate sets of points.
- ExportCSV: Exports coordinates to csv file.
- Render3D: Renders the graph of the attractor.
"""
class Attractor:
    # Initializes class with three arrays of size 10001.
    def __init__(self):
         self.x_values = x_init
         self.y_values = y_init
         self.z_values = z_init
     
    # Euler's Method:
    def EulerMethod(self, function_name):
         for i in range(num_steps):
             x_prime, y_prime, z_prime = function_name(self.x_values[i], self.y_values[i], self.z_values[i])
             self.x_values[i + 1] = self.x_values[i] + (x_prime * step)
             self.y_values[i + 1] = self.y_values[i] + (y_prime * step)
             self.z_values[i + 1] = self.z_values[i] + (z_prime * step)
               
    # Exports arrays to CSV:
    def ExportCSV(self):
         print "Please print a file name below. The extension (csv) is automatically added. \
         Leaving the prompt blank will create a file with the name exports.csv."
         file_name = raw_input("File name: ") + ".csv"
         rows = zip(self.x_values, self.y_values, self.z_values)
         # Check if file name exists. If not, set it to default.
         if file_name[:-3] == '':
             file_name = 'exports.csv'
         else:
             continue
         # File writer:
         with open(file_name, 'wb') as f:
             writer = csv.writer(f)
             for row in rows:
                 writer.writerow(row)
                
    # Renders the Graph:
    def Render3D(self):
          Render(self.x_values, self.y_values, self.z_values)

class Rossler(Attractor):
    # Initializes class with three coefficients.
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    # Rossler Attractor function:
    def Rossler(self, x, y, z):
          x_prime = (-1*y) - z
          y_prime = x + self.a*y
          z_prime = self.b + z*(x-self.c)
          return x_prime, y_prime, z_prime