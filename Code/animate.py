#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:43:12 2020

@author: Elzette
"""

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import interact
import numpy as np






def animate(i): 
    
    vel,t,people = interact.solve(3)
    
    for i in range(len(people)): 
        dhist = np.array(people[i].dhist).transpose()
        
        x = dhist[0][1:]
        y = dhist[1][1:]
        
        p = sns.plot(x, y, color="r")
        p.tick_params(labelsize=17)
        plt.setp(p.lines,linewidth=7)
 
    
    
def animationn():
    

    Writer = animation.FFMpegWriter(fps=30, codec='libx264')  #or 
    

    fig = plt.figure(figsize=(10,6))
    plt.xlim(0, 50)
    plt.ylim(0, 50)
    plt.xlabel('X_Coordinate',fontsize=20)
    plt.ylabel('Y_Coorddinate',fontsize=20)
    plt.title('Path of Individual',fontsize=20)
    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=17, repeat=True)
    #ani.show()
    ani.save('Paths.mp4', writer= Writer)
    
    
    
    
    
    