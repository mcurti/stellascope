# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:08:51 2020

@author: curti
"""

import win32com.client      #needed to load COM objects

#Identyfikator sterownika
#ASCOM.Simulator.Telescope
tel = win32com.client.Dispatch("ASCOM.MeadeGeneric.Telescope")
