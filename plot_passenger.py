# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:36:33 2021

@author: Marco
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import time_slots


database_taxi = pd.read_csv('yellow_tripdata_2020-02.csv') 
#riduco database 
del database_taxi['VendorID']
del database_taxi['DOLocationID']
del database_taxi['trip_distance']
del database_taxi['tpep_dropoff_datetime']
del database_taxi['RatecodeID']
del database_taxi['store_and_fwd_flag']
del database_taxi['payment_type']
del database_taxi['fare_amount']
del database_taxi['extra']
del database_taxi['mta_tax']
del database_taxi['tip_amount']
del database_taxi['tolls_amount']
del database_taxi['improvement_surcharge']
del database_taxi['total_amount']
del database_taxi['congestion_surcharge']
    
    #genero i time slots
fasce_orarie = time_slots.time_slots(database_taxi)
    
def plot_passenger(fasce_orarie):
        #data
        labels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        #trasformo la colonna passenger count di time slots in un array
        array = fasce_orarie[["passenger_count"]].to_numpy()
        # da array passo a lista per inserirli come valori del grafico a barre
        values = array.flatten().tolist()
        
        #plot della figura
        plt.figure(figsize=(7,5),)
        bars = plt.bar(labels, values,width=0.5, align='center',color='blue')
        
        plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
        plt.xlabel('time slots')
        plt.ylabel('passengers')
        
        #salva la figura nella cartella Output
        plt.savefig('Output/barchart.png', dpi=300)
        plt.show()

        return

grafico = plot_passenger(fasce_orarie)
        
        
        
        