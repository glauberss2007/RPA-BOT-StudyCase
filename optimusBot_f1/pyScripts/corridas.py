import pandas as pd
import json

def dfCorridas(dict):
    data = json.loads(dict['Body'])
    data = data['MRData']['RaceTable']
    df_final = pd.DataFrame(columns=['season', 'round', 'url', 'raceName', 'circuitRef', 'lat', 'long', 'locality', 'country'])
    for i in range(len(data['Races'])):
        dic1 = [data['Races'][i]['season'], data['Races'][i]['round'], data['Races'][i]['url'], data['Races'][i]['raceName'], 
                data['Races'][i]['Circuit']['circuitId'], data['Races'][i]['Circuit']['Location']['lat'], 
                data['Races'][i]['Circuit']['Location']['long'], data['Races'][i]['Circuit']['Location']['locality'], 
                data['Races'][i]['Circuit']['Location']['country']]
        data2 = pd.DataFrame(data = dic1).transpose()
        data3 = data2.rename(columns = {0:'season',1:'round',2:'url',3:'raceName', 4:'circuitRef', 5:'lat',
                                        6:'long', 7:'locality', 8:'country'}, inplace = False)
        df_final = df_final.append(data3, ignore_index=True)
    df_final.to_csv(r'C:\Projeto\corridas.csv', index=False)