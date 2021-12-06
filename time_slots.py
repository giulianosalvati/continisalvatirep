# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:54:37 2021

@author: Marco
"""
import pandas as pd 


def time_slots(database_taxi):
    #modifico il tipo della colonna tpep da stringa a datetime
    database_taxi['tpep_pickup_datetime']=pd.to_datetime(database_taxi['tpep_pickup_datetime'])
    #creo un'altra colonna hour che estrae l'ora dal dato datetime presente in tpep
    database_taxi['hour']=database_taxi['tpep_pickup_datetime'].dt.hour
    #elimino le colonne che non servono più (voglio una tabella con solo time slots e somma passeggeri)
    del database_taxi['PULocationID']
    #suddivido in base al valore presente nella colonna hour e per ciascuna sommo il numero di passeggeri
    time_slots = database_taxi.groupby(by=['hour']).sum().groupby(level=0).cumsum()
    
    return time_slots

