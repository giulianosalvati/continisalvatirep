#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:20:42 2021

@author: mariaelenacontini
"""

import Utils
from df_function import CleanData,risult_plot_passenger,timeSlots,crea_lista_df_borough
from time import perf_counter
"""
Quali sono le fasce orarie con più passeggeri? E quella con meno? 
Impostate le vostre fasce orarie (per esempio ogni ora) e scoprite quali sono quelle in cui i taxi 
guidano il maggior numero di passeggeri e ripetete l'analisi per ogni borough. 
Fornite i risultati attraverso un file e un plot. 
Input: anno, mese*, borough*
Output: file, grafico
"""
if __name__ == '__main__':
    
    args = Utils.initializeParser()
    year = Utils.getYearFromParser(args.year)
    month = Utils.getMonthFromParser(args.month)
    fileName = Utils.generateFileName(year, month)
    
    t_start = perf_counter() # tempo di inizio
    
    data_taxi = Utils.readCsv(fileName)
    
    cleaner = CleanData(data_taxi, year,month)
    data_taxi = cleaner.CleanDataframe() # elimino dal dataframe le colonne che non mi interessano
    data_taxi = cleaner.zero_passenger()# elimino tutti i dati con zero passeggeri
    lista_df_borough=crea_lista_df_borough(data_taxi,args.borough) # Creo un lista di dataframe relativi ai dati di ciascun borough o del borough desiderato se richiesto
    fasce_orarie = timeSlots(data_taxi)
    risult_plot_passenger(fasce_orarie,lista_df_borough,args.borough) # Plot del dataframe di New York e dei borough
    
    dt = perf_counter() - t_start # tempo di esecuzione    
       
    print('Tempo di esecuzione: ' + str(dt) + ' s')
    
    print('Fine')