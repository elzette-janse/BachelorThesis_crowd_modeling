#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:02:41 2020

@author: Elzette


    
"""


import numpy as np



def social_force(people,n):
    """ returns vector with social force felt by all agents, fix me"""
    
     #list of all people
    interaction = [[np.zeros(n)for i in range(n)] for i in range(2) ]#list of interaction of people
    
    for i in range(n):
        person = people[i]
        for j in range(n):
            if j==i: 
                interaction[0][i][j] = 0 #store x component of force 
                interaction[1][i][j] = 0 #store y component of force 
            else:
                friend = people[j]
                force = person.repulsive(friend)
                #force = np.linalg.norm(force) #FIX ME LATER - take xy component or.... 
                interaction[0][i][j] = force[0] #store x component of force 
                interaction[1][i][j] = force[1] #store y component of force 

            
    return np.array([np.array([sum(interaction[0][i]),sum(interaction[1][i]) ]) for i in range(n)])



def total_force(people, obsticles, n):
    """ Calculate total force given set of people and boundaries in environment. 
    For this version, only closest boundary is concedered 
    return 2*n matrix of x,y force for all people"""
    
    interaction = social_force(people,n)
    
    motivationx = [person.motivation()[0] for person in people]
    
    
    motivationy = [person.motivation()[1] for person in people ]
    
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


        
    
