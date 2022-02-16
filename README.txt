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

Per ogni analisi svolta (anno, mese), il programma fornisce in uscita un file corrispondente che indica la fascia oraria con il maggiore ed il minore numero di passeggeri per ogni area di interesse. Se si svolge un'altra analisi su dei dati già precedentemente analizzati, questo file viene sovrascritto con i nuovi risultati; in caso contrario, viene creato un nuovo file.
In aggiunta a questo file l'analisi viene completata con degli istogrammi, salvati in dei file in cui sono specificati il mese e l'anno corrispondenti, che mostrano il numero di passeggeri per ciascuna fascia oraria. Se si specifica in input un particolare borough, viene generato l'istogramma relativo a questo borough e quello relativo a tutta New York; altrimenti, vengono riportati i grafici di tutti i borough di New York.

Per avviare l'analisi bisogna digitare in linea di comando:

> python main.py year -m month -b borough

L'anno, espresso in numero, deve essere necessariamente inserito. Mentre sono opzionali gli input del mese e del borough. Per esprimere questi ultimi due input bisogna inserirli tra apici ''.

È possibile elencare tutte le opzioni digitando:

> python main.py -h



