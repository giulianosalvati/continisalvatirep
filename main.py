#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 10:20:53 2021

@author: giuliano
"""
from datetime import datetime,timedelta
import pandas as pd 
import Utils
from df_function import  CleanDataframe

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
    database_taxi = Utils.readCsv(fileName)
    database_taxi= CleanDataframe(database_taxi, year)
    
    

    
    print('Fine')

