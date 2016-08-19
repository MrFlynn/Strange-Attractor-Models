#!python2.7

"""
Nick Pleatsikas : Differential Equations
3D Model Generating:
    
Renders 3D graphs in space of strange attractors given arrays of x,y,z.
"""

# Libraries:
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def render(x_cords, y_cords, z_cords):
    # Initialize the plot:
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    # Set titles:
    ax.set_title('Rossler Attractor')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    # Plot the points:
    ax.plot(x_cords, y_cords, z_cords)

    # Show the graph:
    plt.show()
