import pandas as pd
import json

def dfConstrutores(dict):
    data = json.loads(dict['Body'])
    data = data['MRData']['RaceTable']
    df_final = pd.DataFrame(columns=list(data['Races'][0].keys()))
    for i in range(len(data['Constructors'])):
        data2 = pd.DataFrame(data = list(data['Constructors'][i].values())).transpose()
        data3 = data2.rename(columns = {0:'constructorId',1:'url',2:'name',3:'nationality'}, inplace = False)
        df_final = df_final.append(data3, ignore_index=True)
    df_final.to_csv(r'C:\Users\Usuario\Desktop\Temp\Projeto\construtores.csv', index=False)