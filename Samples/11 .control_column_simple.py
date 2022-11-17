path=r'C:\Users\s.kian\OneDrive - Intrum Law\Desktop\Maurizio'
path1=r'C:\Users\s.kian\OneDrive - Intrum Law\Desktop\Maurizio\Results'
import pandas as pd
import os
files = os.listdir(path)
files_xlsx = [f for f in files if (f[-4:].lower() == 'xlsx')]
len(files_xlsx)
clm=[' SCO ', ' ACCNUM ', ' PRD ', ' Incasso ', ' Data Incasso ',
       ' Codice Causale ', ' Descrizione ', 'Unnamed: 7']
lis=[]
NDG=[]
Posizione=[]
ATTIVITA=[]
REDDITO=[]
for i in files_xlsx:
    df=pd.read_excel(path+'\\'+i)
    c=0
    for j in clm:
        if j in df.columns:
            c+=1
    lis.append(c)
