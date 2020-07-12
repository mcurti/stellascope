# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 15:05:56 2020

@author: mcurti
"""
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

mylocation = EarthLocation(lat=51.4*u.deg, lon=5.4*u.deg, height=67*u.m)
m33 = SkyCoord.from_name('M33')



time = Time('2020-7-11 23:08:00') 

SC = SkyCoord(5.4*u.deg, 51.4*u.deg, obstime = time)
Capella = SC.from_name('Capella')

Capellaaltaz = Capella.transform_to(AltAz(obstime=time, location=mylocation))
m33altaz = m33.transform_to(AltAz(obstime=time, location=mylocation))
# m33altaz = m33.transform_to(time)d