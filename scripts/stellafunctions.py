# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 00:00:00 2020

@author: curti
"""

def get_RA_Dec(txt):
    i = txt.find("HA/Dec")
    raw = txt[(i+11):(i+37)]
    
    h = int(raw[0:2])
    m = int(raw[3:5])
    s = float(raw[6:11])
    
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