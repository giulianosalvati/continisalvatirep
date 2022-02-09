# README

# Research Questions - Gruppo 2

Quali sono le fasce orarie con più passeggeri? E quella con meno? 
Impostate le vostre fasce orarie e scoprite quali sono quelle in cui i taxi
guidano il maggior numero di passeggeri e ripetete l'analisi per ogni borough.
Fornite i risultati attraverso un file e un plot. 
Input: anno, mese*, borough*
Output: file, grafico

# Programma implementato

Il codice considera come fascia oraria ogni ora.

In uscita al programma c'è un file che indica la fascia oraria con il maggiore ed il minore numero di passeggeri per ogni area di interesse. In aggiunta a questo l'analisi viene completata con degli istogrammi che per New York e per ogni borough (se non viene specificato un borough in particolare tra gli input) mostra il numero dei passeggeri per ogni fascia oraria.

Per avviare l'analisi bisogna digitare in linea di comando:

> python main.py year -m month -b borough

L'anno, espresso in numero, deve essere necessariamente inserito. Mentre sono opzionali gli input del mese e del borough. Per esprimere questi ultimi due input bisogna inserirli tra apici ''.

È possibile elencare tutte le opzioni digitando:

> python main.py -h



