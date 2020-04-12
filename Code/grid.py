#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:59:07 2020

@author: Elzette
"""
import numpy as np

def get_neighbours(a):
    x = a[0]
    y = a[1] 
    return [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y+1],[x,y-1],[x+1,y-1],[x+1,y],[x+1,y+1]]

def is_in(position):
    #This is a cheat
    x = int(abs(position[0]//10))
    y = int(abs(position[1]//10))
    return [x,y]


def social(people):
    
    social = []
    grid = [[[] for i in range(120)]for i in range(120)]
    for person in people:
        pos = is_in(person.position)
        grid[pos[0]][pos[1]].append(person)
        
    for person in people:
        neigh = get_neighbours(is_in(person.position))
        force = np.zeros(2)
        for item in neigh:
            if item[0] and item[1] <= 120:
                for human in grid[item[0]][item[1]]:
                    force += person.repulsive(human)  
        social.append(10*force)

    return(social)
    

def total_force(people, obsticles, n):
    """ Calculate total force given set of people and boundaries in environment. 
    For this version, only closest boundary is concedered 
    return 2*n matrix of x,y force for all people"""
    
    interaction = social(people)
    
    motivationx = [person.motivation[0] for person in people]
    
    motivationy = [person.motivation[1] for person in people]
    
    motivation = np.array([motivationx, motivationy ] )
    
    boundaries = []
  
    
    
    for i in range(n):
        person = people[i]
        if len(obsticles) >= 1:
            boundary = np.array([float(0),float(0)])
            
            for item in obsticles:
                boundary += np.array(person.boundary(item[0],item[1]))
            boundaries.append(boundary)
        else: boundaries.append(np.zeros(2))
    
    
    
    boundaries = np.array(boundaries)
    interaction = np.array(interaction )
    motivation = np.array(motivation.transpose())
    
    
 
    return interaction+motivation+boundaries
    
    
                
            
        
    
    
    