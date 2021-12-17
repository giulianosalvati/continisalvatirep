#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:19:39 2021

@author: mariaelenacontini
"""
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

class CleanData:
    
    def __init__(self,database_taxi,year,month):
        self.database_taxi = database_taxi
        self.year = year
        self.month = month
    
    def CleanDataframe(self):
    
        """
        sottoprogramma che in base all'anno e al mese che vengono inseriti in input
        (quelli del file) elimina eventuali dati che non sono di tale periodo.
        Abbiamo tenuto conto della data in cui il passeggero è salito nel taxi
        """
        
        self.database_taxi['tpep_pickup_datetime'] = pd.to_datetime(self.database_taxi['tpep_pickup_datetime'])
        self.database_taxi['year'] = self.database_taxi['tpep_pickup_datetime'].dt.year  
        self.database_taxi['month'] = self.database_taxi['tpep_pickup_datetime'].dt.month                             
        self.database_taxi = self.database_taxi[self.database_taxi['year'] == datetime.strptime(str(self.year), '%Y').year] 
        self.database_taxi = self.database_taxi[self.database_taxi['month'] == datetime.strptime(str(self.month), '%m').month]
        del self.database_taxi['year']
        del self.database_taxi['month']
                           
        return self.database_taxi
    
    def zero_passenger(self,):
        
        """
        sottoprogramma che elimina eventuali dati con 0 passeggeri
        """
        
        self.database_taxi = self.database_taxi[self.database_taxi['passenger_count'] > 0]
        return self.database_taxi
    
# Utile.writeJsonFile(features_df)  
    
def timeSlots(database_taxi):
    """
    Sottoprogramma che somma il numero dei passeggeri durante ciascuna fascia oraria.
    Per le fascie orarie abbiamo tenuto conto di slot da un'ora ciascuno (quindi 24 slots)
    """
        
    #creo una colonna 'hour' che estrae l'ora dalla colonna 'tpep_pickup_datetime' del df
    database_taxi['hour']= database_taxi['tpep_pickup_datetime'].dt.hour
    #elimino le colonne che non servono più (voglio una tabella con solo time slots e somma passeggeri)
    del database_taxi['PULocationID']
    #suddivido in base al valore presente nella colonna hour e per ciascuna sommo il numero di passeggeri
    time_slots = database_taxi.groupby(by=['hour']).sum().groupby(level=0).cumsum()
        
    return time_slots
    
def plot_passenger(fasce_orarie,lista_df_borough,nome_borough):
        
    """
    Sottoprogramma che fa il plot dei dati del dataframe data_taxi e dei borough di interesse
    di modo da rappresentare il numero dei passeggeri (asse y) rispetto alle fasce orarie (asse x).
    Per le fascie orarie abbiamo tenuto conto di slot da un'ora ciascuno (quindi 24 slots)
    """
        
    colori= ['g', 'r', 'c', 'm','y']
    borough=['Manhattan','Queens','Bronx','Staten Island','Brooklyn']
    labels = [*range(0,24,1)]
        
        #trasformo la colonna passenger count di time slots in un array
    array = fasce_orarie[["passenger_count"]].to_numpy()
        # da array passo a lista per inserirli come valori del grafico a barre
    values = array.flatten().tolist()        
        #plot 
    plt.figure(figsize=(7,5))
    plt.title('Yellow Taxi - New York')
    plt.bar(labels, values,width=0.5, align='center',color='blue')        
    plt.xticks(labels)
    plt.xlabel('Time slots')
    plt.ylabel('Passengers')
    #plt.savefig('./output/GraficoYellowTaxi.pdf')
    plt.show()
        
        ### Plot dei boroughs ###
        
    if len(lista_df_borough)>1: # se ho df di piu boroughs
        for k in range(len(lista_df_borough)):
            fasce_orarie = timeSlots(lista_df_borough[k])
            array = fasce_orarie[["passenger_count"]].to_numpy()
            values = array.flatten().tolist()        
            plt.figure(figsize=(7,5))
            plt.title(borough[k])
            plt.bar(labels,values,width=0.5,align='center',color=colori[k])        
            plt.xticks(labels)
            plt.xlabel('Time slots')
            plt.ylabel('Passengers')
            #plt.savefig('./output/Grafico'+borough[k]+'.pdf')
            plt.show()
                            
    else: # se mi interessa solo un borough
        fasce_orarie = timeSlots(lista_df_borough[0])
        array = fasce_orarie[["passenger_count"]].to_numpy()
        values = array.flatten().tolist()        
        plt.figure(figsize=(7,5))
        plt.title(nome_borough)
        plt.bar(labels, values,width=0.5 ,align='center',color='r')        
        plt.xticks(labels)
        plt.xlabel('Time slots')
        plt.ylabel('Passengers')
        #plt.savefig('./output/Grafico'+nome_borough+'.pdf')
        plt.show()
    
def separateBorough(database_taxi,borough_name):
    
    """
    Sottoprogramma che, dati in ingresso il dataframe dei taxi, il dataframe dei codici dei 
    borough e il nome del borough,
    restituisce un dataframe che contiene tutti i dati del dataframe dei taxi che
    hanno come 'PULocationID' un codice che appartiene al borough in ingresso
    """
    
    df_zone= pd.read_csv('indata/taxi+_zone_lookup.csv') # file che contiene i codici rispettivi ad ogni borough
    
    # borough : un df che sarà riempito da eventuali dati che 
    # hanno come 'PULocationID' un codice che corrisponde al borough richiesto
    borough = pd.DataFrame(columns=(database_taxi.columns))
    
    # loc_borough : Lista che sarà riempita di tutti i codici che 
    # corrispondono al borough considerato
    loc_borough = []
    
    # scorro le righe del dataframe delle zone in modo da riempire la lista 
    # loc_borough definita precedentemente
    for i,zona in df_zone.iterrows():
        if zona[1] == borough_name:  # se il codice corrisponde al borough...
            loc_borough = loc_borough + [zona[0]]  # ..aggiungo il codice alla lista
    borough = database_taxi[database_taxi['PULocationID'].isin (loc_borough)]   
    return borough
  
def crea_lista_df_borough(data_taxi,borough_name):
    
    """
    Sottoprogramma che ha in ingresso il df dei viaggi e il nome del borough (se 
    inserito) o altrimenti None (di default).
    Restituisce un lista di dataframe relativi ai viaggi in ciascun borough se 
    non è specificato quello desiderato, altrimenti il df di quello richiesto
    """
    
    lista_df_borough=[]
    borough=['Manhattan','Queens','Bronx','Staten Island','Brooklyn']
    if borough_name is None: # Se in ingresso non viene specificato alcun borough
        for name in borough:
            df_borough=separateBorough(data_taxi,name)
            lista_df_borough.append(df_borough)
    else:
        borough_richiesto = separateBorough(data_taxi, borough_name)
        lista_df_borough.append(borough_richiesto)
    return lista_df_borough

class CalcoloEstremi():
     
    def __init__(self,fasce_orarie):
        self.fasce_orarie = fasce_orarie
    
    def calcola_il_max(self):
        massimo=self.fasce_orarie.loc[self.fasce_orarie['passenger_count'].idxmax()]
        return massimo
    
    def calcola_il_min(self):
        minimo=self.fasce_orarie.loc[self.fasce_orarie['passenger_count'].idxmin()]
        return minimo
        
    


