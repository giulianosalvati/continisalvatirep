# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:36:33 2021

@author: Marco
"""

import matplotlib.pyplot as plt


def plot_passenger(fasce_orarie):
        #data
        labels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        #trasformo la colonna passenger count di time slots in un array
        array = fasce_orarie[["passenger_count"]].to_numpy()
        # da array passo a lista per inserirli come valori del grafico a barre
        values = array.flatten().tolist()
        
        #plot della figura
        plt.figure(figsize=(7,5),)
        plt.bar(labels, values,width=0.5, align='center',color='blue')        
        plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
        plt.xlabel('time slots')
        plt.ylabel('passengers')
        plt.show()

        
        
        
        