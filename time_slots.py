# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:54:37 2021

@author: Marco
"""
import pandas as pd 

def reduced_database_passeger_count(database_taxi):
    """ 
    Elimino tutte le colonne del dataframe che non mi interessano. 
    Tengo in considerazione solo le colonne:
        tpep_pickup_datetime 
        passenger_count 
        PULocationID 
    
    """
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
    return database_taxi


database_taxi = pd.read_csv('yellow_tripdata_2020-02.csv').head(80) 
database_taxi = reduced_database_passeger_count(database_taxi)

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

fasce_orarie = time_slots(database_taxi)