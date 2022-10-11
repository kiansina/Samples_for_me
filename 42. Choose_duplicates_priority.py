path1=r'C:\Users\s.kian\OneDrive - Intrum Law\Desktop\MasterPlan\results'
import pandas as pd
from numpy import nan
dg=pd.read_excel(path1+'\\Unique_patr.xlsx')
df=pd.read_excel(path1+'\\silish.xlsx')

df['Titolarità_Stato'].fillna('Irrilevante',inplace=True)
df.Titolarità_Stato=pd.Categorical(df.Titolarità_Stato,
                              categories=['Proprieta', 'Nuda Proprieta', 'Irrilevante'],
                              ordered=True)

dff = df.sort_values('Titolarità_Stato').groupby(['RIF1', 'Codice Fiscale'], as_index=False).first()

with pd.ExcelWriter(path1+'\\Reddituali_Catasto.xlsx') as writer:
    dg.to_excel(writer, sheet_name='Reddituali')
    dff.to_excel(writer, sheet_name='Catasto')
