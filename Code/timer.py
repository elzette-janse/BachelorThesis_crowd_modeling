#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 13:55:20 2020

@author: Elzette
"""
import time
import interact
import matplotlib.pyplot as plt

def timer(k):
    running = []
    for i in range(1,50): 
        print(i)
        start_time = time.time()
        people, t_list = interact.solve(i,k)
        running.append(time.time() - start_time)
    
    plt.plot(running)
    plt.xlabel('Number of People')
    plt.ylabel('Running Time')
    plt.title('Running time  Obsticles')
    return running