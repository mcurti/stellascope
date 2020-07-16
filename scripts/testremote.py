# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:58:03 2020

@author: curti
"""
import stellafunctions as s
import win32com.client      #needed to load COM objects



tel = win32com.client.Dispatch("ASCOM.Simulator.Telescope")
tel.connected = True
tel.tracking = True
s.go_to(tel, "Moon")


#ASCOM.Simulator.Telescope
# tel = win32com.client.Dispatch("ASCOM.MeadeGeneric.Telescope")

