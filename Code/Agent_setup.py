#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:22:39 2020

@author: Elzette
""" 
import numpy as np
import random
import boundary_dist as bd

class Person():
    
    A = 7
    a1 = 3
    B = .5
    relax_t = 1
    
    def __init__(self):
        
        self.position = np.array([random.uniform(0,20), random.uniform(0,20)])
        self.target = np.array([100,100])
        self.radius = .05
        
        self.max_speed = 7
        self.velocity = np.array([float(0.00), random.random()])
        self.speed = np.linalg.norm(self.velocity)
   
        self.accel = np.array([0,0])
        
        self.direction = (self.target - self.position)/ \
        np.linalg.norm(self.target - self.position)
        
        
        
        self.vhist = []
        self.dhist = []
        self.shist = []
    
    
    def distance(self,b):
        return np.linalg.norm(self.position-b.position)

        
 
    def repulsive(self,a):
        if  np.linalg.norm(self.target - self.position) >= 5:
            f1 =  self.A*np.exp( (self.radius+a.radius-self.distance(a))/self.B ) #magnitude force 
            eta = (self.position - a.position)/np.linalg.norm(self.distance(a)) #normalize components 

            lambd = .4 #anisotropic character 
            F = lambd + (1-lambd)*(1+np.dot(eta,self.velocity)/2) #anisotropic behavior of person
            return 5*self.A*f1*F/np.linalg.norm(self.velocity)*eta + self.a1*f1*eta
        return np.zeros(2)

    
    def boundary(self,start,end):
        #take nearest point        
        
        if np.linalg.norm(self.target - self.position) >= 5:
            (direct, nearest,dista) = bd.pnt2line(self.position,start,end)
            if dista > 0.1:
                return 20*self.a1*np.exp(self.radius-dista)*np.array(direct)#timesperp vect boundary and self
            return 200*np.ones(2)*self.a1*np.exp(self.radius-dista)*np.array(direct)
        return np.zeros(2)
        
        
    def motivation(self):
        
        if np.linalg.norm(self.target - self.position) >= 5: 
            return (self.max_speed * self.direction - self.velocity )\
                /self.relax_t #option here to redefine v_max with impatience and obsticle
        return np.zeros(2)


    