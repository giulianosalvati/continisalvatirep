#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 10:20:53 2021

@author: giuliano
"""

import numpy  as np
import pandas as pd 

# def ReadJsonFile(file):
#     try:
#         database = pd.csv_json(file)
#         return log_list
#     except:
#         print('Could not load the file! \nThe specified file path-name does not exist!')
#         sys.exit()

database_taxi_ridotto = pd.read_csv('/Users/giuliano/Desktop/yellow_tripdata_2020-01.csv').head(80)
