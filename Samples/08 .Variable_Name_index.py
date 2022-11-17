
df=pd.read_excel(r"C:\Users\sina.kian\Desktop\Paola\NDB\pyv1.xlsx")


arraysDict={}
for i in np.arange(25,125,25):
    A=df['Production Plant'].unique()[:i]
    B=df[df['Production Plant']==A[-1:][0]].index[-1]
    print(B)
    arraysDict['df{}'.format(i)] = df[:B+1]


df1=arraysDict['df25']
df2=arraysDict['df50']
df3=arraysDict['df75']
df4=arraysDict['df100']
