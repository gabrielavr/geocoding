#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:17:34 2018

@author: jose
"""

import pandas as pd
import geocoder
import time

#con pandas se lee el csv
data = pd.read_csv("addresses_test.csv", header=None)
#se agregan las columnas de latitud y longitud al dataframe
data.columns = ['direccion']
data = data.assign(latitud=None, longitud=None)
#para cada elemento, se geocodifica y se guarda en el dataframe
for index, row in data.iterrows():
    print(row['direccion'],row['latitud'])
    # Apply some sleep to ensure to be below 50 requests per second
    time.sleep(1)
    #se usa la función geocoder con ArcGIS como servidor y se le pasa como entrada la dirección. Con df.ix se accede a una celda concreta
    g = geocoder.arcgis(data.ix[index,'direccion'])
    #para cada resultado en g (puede haber más de uno - cambiar luego)
    print(g.latlng)
    #se escribe en la celda concreta con df.at
    data.at[index,'latitud'] = g.lat
    data.at[index,'longitud'] = g.lng
        

#guardar en un csv/xls
data.to_excel("addresses_geocoded.xlsx",index = False)        
