#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 10:20:53 2021

@author: giuliano
"""
import datetime
import numpy  as np
import pandas as pd 

"""
Quali sono le fasce orarie con più passeggeri? E quella con meno? 
Impostate le vostre fasce orarie (per esempio ogni ora) e scoprite quali sono quelle in cui i taxi 
guidano il maggior numero di passeggeri e ripetete l'analisi per ogni borough. 
Fornite i risultati attraverso un file e un plot. 
Input: anno, mese*, borough*
Output: file, grafico
"""

# def ReadJsonFile(file):
#     try:
#         database = pd.csv_json(file)
#         return log_list
#     except:
#         print('Could not load the file! \nThe specified file path-name does not exist!')
#         sys.exit()

database_taxi_ridotto = pd.read_csv('/Users/giuliano/Desktop/yellow_tripdata_2020-01.csv').head(80)

#ordino, in base alla data di partenza,  prendendo in considerazione la data di partenza e il numero di passeggeri a carico
interessed_df= database_taxi_ridotto[[ 'tpep_pickup_datetime','passenger_count']].sort_values(by=['tpep_pickup_datetime'])

#converto la colonna della data di ingresso in formato datetime più utile
interessed_df['tpep_pickup_datetime']=pd.to_datetime(interessed_df['tpep_pickup_datetime'])

#come eliminare  date che non sono di mio interesse
#creo una data di soglia(un minuto prima dell'anno che sto considerando) e ripulisco il dataset
limit_day= pd.to_datetime('2019-12-31 23:59:59')
interessed_df=interessed_df.drop(interessed_df[interessed_df.tpep_pickup_datetime < limit_day].index

#resta da confrontare il dataframe con le fasce orarie di interesse e calcolare quelle con più/meno passeggeri