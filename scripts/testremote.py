# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:58:03 2020

@author: curti
"""
import stellafunctions as s
import requests
import win32com.client      #needed to load COM objects



url_main = "http://localhost:8090/api/"

url_status = "main/status"
url_find   = "objects/find?str=moon"
url_info   = "objects/info?name=Capella"
    
response= requests.get(url_main + url_info)
ra, dec = s.get_RA_Dec(response.text)

print(ra, dec)


#ASCOM.Simulator.Telescope
# tel = win32com.client.Dispatch("ASCOM.MeadeGeneric.Telescope")

