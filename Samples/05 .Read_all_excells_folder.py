import os
import pandas as pd
path = os.getcwd()
files = os.listdir(path)
files
files_xlsx = [f for f in files if f[-4:] == 'xlsx']
files_xlsx
df = pd.DataFrame()
for f in files_xls:
    data = pd.read_excel(f, 'Sheet1')
    df = df.append(data)
