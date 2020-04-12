#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:41:10 2020

@author: Elzette
"""



def border():
    return[[(float(0),float(120)),(float(0),float(0))], [(float(0),float(0)),(float(120),float(0))],
    [(float(120),float(120)),(float(0),float(120))], [(float(120),float(120)),(float(120),float(0))]
    ]

def environment(K):
    
    if K == 10:
        #4 doors
        return [ [(float(40),float(40)),(float(55),float(40)) ],
                  [(float(60),float(40)),(float(70),float(40)) ],
                  [(float(40),float(70)),(float(55),float(70)) ], 
                  [(float(60),float(70)),(float(70),float(70)) ], 
                  [(float(40),float(40)),(float(40),float(55)) ],
                  [(float(40),float(60)),(float(40),float(70)) ],
                  [(float(70),float(40)),(float(70),float(55)) ], 
                  [(float(70),float(60)),(float(70),float(70)) ]
                  
                  ] 
    
    if K == 9:
        return environment(0)
    
    if K ==8:
        return environment(5)
    
    
    if K == 0:
        return []
    
    if K == 1:
        #line
        return [[(float(40),float(20)),(float(40),float(40))]]
    
    
    if K == 2:
        #90 degree corner 
        return [[(float(0),float(20)),(float(40),float(20))],
                [(float(40),float(20)),(float(40),float(60))]]

    if K ==4: 
        ## hallway modified 
        return [[(float(0),float(20)),(float(40),float(20))],
                [(float(40),float(20)),(float(40),float(60))], 
                [(float(60),float(20)),(float(60),float(60))],
                [(float(60),float(20)),(float(100),float(20))]]
    if K ==5: 
        ## hallway modified ( more broad)
        return [[(float(-100),float(20)),(float(40),float(20))],
                 [(float(40),float(20)),(float(40),float(60))], 
                 [(float(70),float(20)),(float(70),float(60))],
                 [(float(70),float(20)),(float(100),float(20))],
                 [(float(0),float(60)),(float(40),float(60))]]
    
    
    if K ==6: 
        #4 way crossing
        return [
                 #top left corner 
                 [(float(0),float(70)),(float(35),float(70))], 
                 [(float(35),float(100)),(float(35),float(70))],
                 
                 
                 #bottom left corner 
                 [(float(0),float(40)),(float(35),float(40))], 
                 [(float(35),float(40)),(float(35),float(0))],
                 
                 
                 #top right corner 
                 [(float(70),float(100)),(float(70),float(70))], 
                 [(float(70),float(70)),(float(100),float(70))],
                 
                 
                 #bottom right corner 
                 [(float(70),float(40)),(float(70),float(0))], 
                 [(float(70),float(40)),(float(100),float(40))],
                 
                 
                 ]
        
        
    if K ==7:
        #small gate
        return [ [(float(50),float(60)),(float(60),float(200)) ] , 
                
                [(float(50),float(-100)),(float(50),float(50)) ]]
    
        