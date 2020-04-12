#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:36:26 2020

@author: Elzette
"""
import copy
import numpy as np
import math

def RK_step(y, h, f, people, obsticles,n):
    
    k = []
    
    k.append(np.array(h * f(people,obsticles,n)))
    
    for i in range(1,4): 
        people1 = copy.deepcopy(people)
        for j in range(len(people1)):
            people1[j].velocity = np.array(people1[j].velocity) + 0.5 * k[i-1][j]
            k.append( np.array(h * f(people1, obsticles, n) ) )
               
    y = y + sum(k) / 6

    return y


def RK_solve(h, f, y_0, start_t, end_t, obsticles, people):
    
    n = len(people)
  
    N = int((end_t - start_t) / h) # Number steps
    
    # Following the notation in the theory, we have N+1 discrete time values linearly spaced
    t_list = np.linspace(start_t, end_t, N + 1)
    
    # Initialise array to store y-values for each person 
    y_list = [[ np.zeros(2) for i in range(n)] for i in range(N+1)]
    
    
    # Assign initial condition to first element
    y_list[0] = y_0
    
    
    for j in range(len(people)):
            people[j].shist.append(people[j].speed)
            people[j].dhist.append(people[j].position)
            
    
    # Assign the rest of the array using N Euler_steps
    for i in range( N):
    #fix y_list needs to be a tensor with people, and their history 
        
        step = RK_step(y_list[i], h, f, people, obsticles,n)
        
        
        for j in range(n):
            # Maybe not good here - need to fix!!! (way update position/vel...) 

            
            y_list[i + 1] = step
        
            ### THING BELOW: choose min_norm(speed.max,velocity current)) ###
            #if np.linalg.norm(y_list[i + 1][j]) >  people[j].max_speed:
             #   people[j].velocity = people[j].max_speed * people[j].direction
            #else: 
            
            
            ### use relativity constant to decrease speed###
            #people[j].velocity = y_list[i + 1][j] * 1/(1+math.sqrt(abs(np.linalg.norm(y_list[i+1][j])-people[j].max_speed)))
            
            #### use normal speed 
            people[j].velocity = y_list[i + 1][j]
        
            
            people[j].speed = np.linalg.norm(people[j].velocity)

            people[j].position += h* people[j].velocity
            
    
            
            direc = (people[j].target - people[j].position)/np.linalg.norm(people[j].target - people[j].position)
            
            if np.linalg.norm(people[j].target - people[j].position) >= .05:
                people[j].direction = direc
            else: people[j].direction = np.array([0,0])
            

            
            people[j].shist.append(people[j].speed)
            
            people[j].dhist.append( [float(people[j].position[0]),float(people[j].position[1])] )
            
    return y_list, t_list 