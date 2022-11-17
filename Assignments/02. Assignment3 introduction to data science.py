def answer_one():
    #### YOUR CODE HERE
    import math
    import re
    def isnan(value):
        try:
            return math.isnan(float(value))
        except:
            return True
    df=pd.read_excel(r'assets/Energy Indicators.xls')
    df.columns=df.loc[8]
    df.columns
    df=df[['Country', 'Energy Supply', 'Energy Supply per capita', 'Renewable Electricity Production']]
    df.columns=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    df=df[17:]
    df['Energy Supply']=df['Energy Supply']*1000000
    Energy=df
    Energy.head(50)
    for i in df.index:
        if isnan(df['Energy Supply'].loc[i]):
            df['Energy Supply'].loc[i]=np.NaN
    df.index=range(0,len(df))
    for i in df.index:
        if df['Country'].loc[i]=="Republic of Korea":
            df['Country'].loc[i]="South Korea"
        elif df['Country'].loc[i]=='United States of America':
            df['Country'].loc[i]="United States"
        elif df['Country'].loc[i]=="United Kingdom of Great Britain and Northern Ireland":
            df['Country'].loc[i]="United Kingdom"
        elif df['Country'].loc[i]=="China, Hong Kong Special Administrative Region":
            df['Country'].loc[i]="Hong Kong"
#df5=df[:10]
    #print(i)
    Energy=df
    df5=df['Country']
#df10=df5[df5.str.match('^[\\w ]*\\([\\w ]*\\)')==True]
#df10
    df10=df5
#df10.loc[115]
    df100 = df10.replace(to_replace ='\\ \\([\\w ]*\\)', value = '', regex = True)
    df100
#df100.loc[115]
#df10=df100[df100.str.match('^[\\w ]*\\d')==True]
#df10
#df10.loc[28]
    df100 = df100.replace(to_replace ='\\d', value = '', regex = True)
    df100
    for i in df100.index:
        if df100.loc[i]=="Republic of Korea":
            df100.loc[i]="South Korea"
        elif df100.loc[i]=='United States of America':
            df100.loc[i]="United States"
        elif df100.loc[i]=="United Kingdom of Great Britain and Northern Ireland":
            df100.loc[i]="United Kingdom"
        elif df100.loc[i]=="China, Hong Kong Special Administrative Region":
            df100.loc[i]="Hong Kong"
    Energy['Country']=df100
    GDP=pd.read_csv(r'assets/world_bank.csv')
    GDP.columns=GDP.loc[3]
    GDP=GDP[4:]
    for i in GDP.index:
#    print(i)
        if GDP['Country Name'][i]=="Korea, Rep.":
            GDP['Country Name'][i]="South Korea"
        elif GDP['Country Name'][i]=="Iran, Islamic Rep.":
            GDP['Country Name'][i]="Iran"
        elif GDP['Country Name'][i]=="Hong Kong SAR, China":
            GDP['Country Name'][i]="Hong Kong"
    GDP
    ScimEn=pd.read_excel(r'assets/scimagojr-3.xlsx')
    ScimEn=ScimEn[:15]
#GDP=GDP[['Country Name',   'Country Code', 'Indicator Name', 'Indicator Code','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    col=list(GDP.columns)
    col1=col[:4]
    col2=(col[50:])
    col=col1+col2
    GDP=GDP[col]
    for i in range(0,len(col2)):
        col2[i]=str(int(col2[i]))
    col=col1+col2
    GDP.columns=col
    GDP=GDP.set_index('Country Name')
    ScimEn=ScimEn.set_index('Country')
    Energy=Energy.set_index('Country')
    ScimEn.columns
    DF = pd.merge(ScimEn,Energy, how = 'left', left_index=True, right_index=True)
    GDP=GDP[col2]
    DF = pd.merge(DF,GDP, how = 'left', left_index=True, right_index=True)
    #DF.to_excel('DF.xlsx')
    #print(df.index)
    return DF#df100.loc[216]#Energy[190:]#['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    raise NotImplementedError()
DF=answer_one()
DF







def answer_two():
    EN=pd.read_excel(r'assets/Energy Indicators.xls')
    GD=pd.read_csv(r'assets/world_bank.csv')
    SE=pd.read_excel(r'assets/scimagojr-3.xlsx')
    return len(SE)
    raise NotImplementedError()
answer_two()







def answer_three():
    DF['Average of 10 years'] = DF.mean(axis=1)
    avgGDP=DF['Average of 10 years']
    avgGDP=avgGDP.sort_values()
    return avgGDP
    # YOUR CODE HERE
    raise NotImplementedError()
DF




def answer_four():
    # YOUR CODE HERE
    DF=DF.sort_values('Average of 10 years',ascending=False)
    return DF.iloc[5]['2015']-DF.iloc[5]['2006']
    raise NotImplementedError()
DF


def answer_five():
    # YOUR CODE HERE
    return DF['Energy Supply per Capita'].mean(axis=0)
    raise NotImplementedError()
DF


def answer_six():
    DF["% Renewable"] = pd.to_numeric(DF["% Renewable"])
    return (DF["% Renewable"].idxmax(),DF["% Renewable"].max())
#DF['% Renewable'].dropna().idxmax()
#    # YOUR CODE HERE
    raise NotImplementedError()
DF



def answer_seven():
    DF['Ratio']=DF['Self-citations']/DF['Citations']
    return (DF['Ratio'].idxmax(),DF['Ratio'].max())
#    # YOUR CODE HERE
    raise NotImplementedError()
DF


def answer_eight():
    DF['Pop']=DF['Energy Supply']/DF['Energy Supply per Capita']
    return DF.sort_values('Pop',ascending=False).index[2]
    # YOUR CODE HERE
    raise NotImplementedError()
DF['Pop']=DF['Energy Supply']/DF['Energy Supply per Capita']
DF



def answer_nine():
    DF['Cite per capita']=DF['Citable documents']/DF['Pop']
    DF
    DFF=DF[['Cite per capita','Energy Supply per Capita']]
    DFF=DFF.dropna()
    DFF.corr(method ='pearson')
    return DFF['Cite per capita'].astype('float64').corr(DFF['Energy Supply per Capita'].astype('float64'))
#DF['Cite per capita']=DF['Cite per capita'].astype('float64')\n",
#DF['Energy Supply per Capita']=DF['Energy Supply per Capita'].astype('float64')\n",
#import matplotlib as plt\n",
#DF.plot(x='Cite per capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])\n",

    # YOUR CODE HERE\n",
    raise NotImplementedError()"


def answer_ten():
    # YOUR CODE HERE
    A=DF["% Renewable"].mean()
    DF["New_Column"]=[55]*len(DF)
    for i in DF.index:
        if DF["% Renewable"][i]>A:
            DF["New_Column"][i]=1
        else:
            DF["New_Column"][i]=0
    HighRenew=DF["New_Column"]
    return HighRenew
    raise NotImplementedError()






def answer_eleven():
    ContinentDict  = {'China':'Asia',
                      'United States':'North America',
                      'Japan':'Asia',
                      'United Kingdom':'Europe',
                      'Russian Federation':'Europe',
                      'Canada':'North America',
                      'Germany':'Europe',
                      'India':'Asia',
                      'France':'Europe',
                      'South Korea':'Asia',
                      'Italy':'Europe',
                      'Spain':'Europe',
                      'Iran':'Asia',
                      'Australia':'Australia',
                      'Brazil':'South America'}
    AA = pd.DataFrame(list(ContinentDict.items()))
    AA.columns=['Country','Continent']
    AA=AA.set_index('Country')
    AA
    DFF = pd.merge(DF,AA, how = 'left', left_index=True, right_index=True)
#df.groupby('Company Name').agg(MySum=('Amount', 'sum'), MyCount=('Amount', 'count'))
    DFF=DFF.reset_index()
#*DFF.groupby(\"Continent\")[['Pop','Country']].agg(['sum','count'])
    DFF["Pop"] = pd.to_numeric(DFF["Pop"], downcast="float")
    DFFF=DFF.groupby('Continent').agg(size=('Country', 'count'), Sum=('Pop', 'sum'), mean=('Pop', 'mean'), Std=('Pop','std'))
    return DFFF
#DF
#DE11=DF[['Country','Continent']]
#DE11=DE11.groupby(by=["Continent"]).count()
#DE12=DF[['Continent','Pop']]
#DE12.groupby(by=["Continent"]).sum()
#PV=pd.pivot_table(DF, values='Pop', index=['Continent','Country'], columns=None, aggfunc=[np.sum,np.min])
#PV
#    # YOUR CODE HERE
#    raise NotImplementedError()
DFF = pd.merge(DF,AA, how = 'left', left_index=True, right_index=True)
DFF

def answer_twelve():
#DFF.columns
    ContinentDict  = {'China':'Asia',
                      'United States':'North America',
                      'Japan':'Asia',
                      'United Kingdom':'Europe',
                      'Russian Federation':'Europe',
                      'Canada':'North America',
                      'Germany':'Europe',
                      'India':'Asia',
                      'France':'Europe',
                      'South Korea':'Asia',
                      'Italy':'Europe',
                      'Spain':'Europe',
                      'Iran':'Asia',
                      'Australia':'Australia',
                      'Brazil':'South America'}
    AA = pd.DataFrame(list(ContinentDict.items()))
    AA.columns=['Country','Continent']
    AA=AA.set_index('Country')
    AA
    DFF = pd.merge(DF,AA, how = 'left', left_index=True, right_index=True)
#df.groupby('Company Name').agg(MySum=('Amount', 'sum'), MyCount=('Amount', 'count'))
    DFF=DFF.reset_index()
#*DFF.groupby(\"Continent\")[['Pop','Country']].agg(['sum','count'])
    DFF["Pop"] = pd.to_numeric(DFF["Pop"], downcast="float")
    BB=pd.cut(DFF['% Renewable'],5)
    DW=DFF[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
       'Citations per document', 'H index', 'Energy Supply',
       'Energy Supply per Capita', '2006', '2007', '2008',
       '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       'Average of 10 years', 'Ratio', 'Pop', 'Cite per capita', 'New_Column',
       'Continent']]
    DQ=pd.merge(DW,BB,how='left',left_index=True, right_index=True)
    DQ=DQ.set_index(['Continent','% Renewable'])
    #DQ=DQ['Country']
    DMMM=DQ.groupby(['Continent','% Renewable']).size()
    return (DMMM)
#DW
#    # YOUR CODE HERE
#    raise NotImplementedError()
answer_twelve()
#type(DMMM)




def answer_thirteen():
    # YOUR CODE HERE
    import locale
    locale.setlocale(locale.LC_ALL, '')
#locale.format("%d", 1255000, grouping=True)
    for i in DF.index:
        A=DF['Pop'][i]
        DF['Pop'][i]=locale.format("%d", A, grouping=True)
    PopEst=DF['Pop']

    return PopEst
    raise NotImplementedError()
























    #################
    #def answer_two():
#    EN=pd.read_excel(r'assets/Energy Indicators.xls')
#    EN.columns=EN.loc[8]
#    EN=EN[17:244]
#    GD=pd.read_csv(r'assets/world_bank.csv')
#    GD.columns=GD.loc[3]
#    GD=GD[4:]
#    SE=pd.read_excel(r'assets/scimagojr-3.xlsx')
#    A=len(SE)+len(GD)+len(EN)-3*len(DF)
#    return A
#    raise NotImplementedError()
#answer_two()
def answer_two():
    import math
    import re
    def isnan(value):
        try:
            return math.isnan(float(value))
        except:
            return True
    df=pd.read_excel(r'assets/Energy Indicators.xls')
    df.columns=df.loc[8]
    df.columns
    df=df[['Country', 'Energy Supply', 'Energy Supply per capita', 'Renewable Electricity Production']]
    df.columns=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    df=df[17:244]
    df['Energy Supply']=df['Energy Supply']*1000000
    Energy=df
    Energy.head(50)
    for i in df.index:
        if isnan(df['Energy Supply'].loc[i]):
            df['Energy Supply'].loc[i]=np.NaN
    df.index=range(0,len(df))
    for i in df.index:
        if df['Country'].loc[i]=="Republic of Korea":
            df['Country'].loc[i]="South Korea"
        elif df['Country'].loc[i]=='United States of America':
            df['Country'].loc[i]="United States"
        elif df['Country'].loc[i]=="United Kingdom of Great Britain and Northern Ireland":
            df['Country'].loc[i]="United Kingdom"
        elif df['Country'].loc[i]=="China, Hong Kong Special Administrative Region":
            df['Country'].loc[i]="Hong Kong"
#df5=df[:10]
    #print(i)
    Energy=df
    df5=df['Country']
#df10=df5[df5.str.match('^[\\w ]*\\([\\w ]*\\)')==True]
#df10
    df10=df5
#df10.loc[115]
    df100 = df10.replace(to_replace ='\\ \\([\\w ]*\\)', value = '', regex = True)
    df100
#df100.loc[115]
#df10=df100[df100.str.match('^[\\w ]*\\d')==True]
#df10
#df10.loc[28]
    df100 = df100.replace(to_replace ='\\d', value = '', regex = True)
    df100
    for i in df100.index:
        if df100.loc[i]=="Republic of Korea":
            df100.loc[i]="South Korea"
        elif df100.loc[i]=='United States of America':
            df100.loc[i]="United States"
        elif df100.loc[i]=="United Kingdom of Great Britain and Northern Ireland":
            df100.loc[i]="United Kingdom"
        elif df100.loc[i]=="China, Hong Kong Special Administrative Region":
            df100.loc[i]="Hong Kong"
    Energy['Country']=df100


    GDP=pd.read_csv(r'assets/world_bank.csv')
    GDP.columns=GDP.loc[3]
    GDP=GDP[4:]
    for i in GDP.index:
#    print(i)
        if GDP['Country Name'][i]=="Korea, Rep.":
            GDP['Country Name'][i]="South Korea"
        elif GDP['Country Name'][i]=="Iran, Islamic Rep.":
            GDP['Country Name'][i]="Iran"
        elif GDP['Country Name'][i]=="Hong Kong SAR, China":
            GDP['Country Name'][i]="Hong Kong"

    ScimEn=pd.read_excel(r'assets/scimagojr-3.xlsx')
    ScimEn=ScimEn[:15]

    GDP=GDP.set_index('Country Name')
    ScimEn=ScimEn.set_index('Country')
    Energy=Energy.set_index('Country')
    EE = pd.merge(ScimEn,GDP, how = 'outer', left_index=True, right_index=True)
    EE = pd.merge(EE,Energy, how = 'outer', left_index=True, right_index=True)
    A=len(EE)-len(DF)
    return len(GDP)
answer_two()
