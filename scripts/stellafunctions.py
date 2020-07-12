# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 00:00:00 2020

@author: curti
"""

def get_RA_Dec(txt):
    i = txt.find("RA/Dec (on date)")
    j = txt.find("HA/Dec")
    raw = txt[(i+17):(j-4)]
        
    
    Is = raw.find("    ")
    Ie = raw.find("h")
    h = float(raw[(Is+4):Ie])
    
    
    Is = raw.find("h")
    Ie = raw.find("m")
    m = float(raw[(Is+1):Ie])
    
    
    Is = raw.find("m")
    Ie = raw.find("s")
    s = float(raw[(Is+1):Ie])
    
    Is = raw.find("/")
    Ie = raw.find("°")
    dd = float(raw[(Is+1):(Ie-1)])
    
    Is = raw.find("°")
    Ie = raw.find("'")
    mm = float(raw[(Is+1):(Ie)])/60
    
    
    Is = raw.find("'")
    Ie = raw.find("\"")
    ss = float(raw[(Is+1):(Ie)])/(60*60)
    
    ra = h+(m + s/60)/60
    dec = dd+mm+ss
    return ra, dec