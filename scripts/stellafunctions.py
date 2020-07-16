# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 00:00:00 2020

@author: curti
"""
import requests

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
    sign = raw[Is+1]
    
    Is = raw.find("°")
    Ie = raw.find("'")
    mm = float(sign+raw[(Is+1):(Ie)])/60
    
    
    Is = raw.find("'")
    Ie = raw.find("\"")
    ss = float(sign+raw[(Is+1):(Ie)])/(60*60)
    
    ra = h+(m + s/60)/60
    dec = dd+mm+ss
    return ra, dec

def go_to(tel, body):
    url_main = "http://localhost:8090/api/"
    url_info   = "objects/info?name=%s" % body
    
    response= requests.get(url_main + url_info)
    
    ra, dec = get_RA_Dec(response.text)
    
    tel.slewtocoordinates(ra, dec)
    