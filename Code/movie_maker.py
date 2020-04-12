#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:35:12 2020

@author: Elzette
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:54:17 2020

@author: Elzette
"""

from matplotlib import pyplot as plt
from celluloid import Camera
from matplotlib.animation import  PillowWriter
import interact
import numpy as np

people, t_list = interact.solve(5,2)

dhist = [person.dhist for person in people]

fig = plt.figure() 
camera = Camera(fig)
n = len(people)


for j in range(1,len(t_list)):
    
       
       for i in range(0,n):     
           dhist = np.array(people[i].dhist).transpose()
           plt.scatter(dhist[0][j], dhist[1][j], label= i , linewidth=1, color = 'blue' )
           
       plt.xlabel('x_component')
       plt.ylabel('y_component')
       
       plt.plot([float(0),float(40),float(40)],
                [float(20),float(20),float(60)], color = 'red')
       plt.title("Bird's Eye Path of Individuals")
       #plt.show()
       camera.snap()
    
animation = camera.animate()
animation.save( 'corner_5RK.gif', writer = PillowWriter(fps=40) )