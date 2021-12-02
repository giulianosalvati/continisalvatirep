#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:25:23 2021

@author: giuliano
"""

import pandas as pd
from datetime import datetime,timedelta

def CleanDataframe(data_frame, year):
    data_min= datetime.strptime(str(year), '%Y')
    data_frame['tpep_pickup_datetime']= pd.to_datetime(data_frame['tpep_pickup_datetime'])
    data_frame=  data_frame[data_frame.tpep_pickup_datetime > data_min]
    return data_frame
 
  
  