path=r'C:\Users\s.kian\OneDrive - Intrum Law\Desktop\Angela_romano'
path1=r'C:\Users\s.kian\OneDrive - Intrum Law\Desktop\Angela_romano\Results'
import pandas as pd
import os
files = os.listdir(path)
files_xlsx = [f for f in files if (f[-4:].lower() == 'xlsx')]
len(files_xlsx)
clm=['NDG', 'Posizione', 'ATTIVITA\' LAVORATIVA', 'REDDITO mensile']
lis=[]
NDG=[]
Posizione=[]
ATTIVITA=[]
REDDITO=[]
for i in files_xlsx:
    a=0
    b=0
    c=0
    d=0
    df=pd.read_excel(path+'\\'+i)
    if ('NDG' in df.columns) or ('ndg' in df.columns):
        a=1
    if ('Posizione' in df.columns) or ('Nome' in df.columns) or(
    'NOME' in df.columns) or ('Soggetto da Rintracciare' in df.columns):
        b=1
    if 'ATTIVITA\' LAVORATIVA' in df.columns:
        c=1
    if ('REDDITO mensile' in df.columns) or (
    'REDDITO LORDO' in df.columns) or(
    'REDDITO'  in df.columns) or(
    'REDDITO LORDO ' in df.columns) or ('reddito' in df.columns):
        d=1
    NDG.append(a)
    Posizione.append(b)
    ATTIVITA.append(c)
    REDDITO.append(d)
    lis.append(i)

list_of_tuples = list(zip(lis,NDG, Posizione, ATTIVITA, REDDITO))
A=pd.DataFrame(list_of_tuples,columns=['I', 'NDG', 'Posizione', 'ATTIVITA\' LAVORATIVA', 'REDDITO mensile'])
A[A['REDDITO mensile']==0]
