import pandas as pd
import json

# url = http://ergast.com/api/f1/results.json?limit=30&offset=30

def dfResultados(dict):
  data = json.loads(dict['Body'])
  data = data['MRData']['RaceTable']
    
  # criando colunas do dataframe
  df_final = pd.DataFrame(columns = ['season', 'raceName', 'circuitRef','date', 'position', 
                                      'points', 'driverRef', 'construtor', 'grid', 'laps', 
                                      'status', 'millis', 'time'])
  # primeiro nó
  for i in range(len(data['Races'])):
    dic2 = data['Races'][i]
    #lista com os valores do dicionario (primeiro nó)
    dados_race1 = [dic2['season'], dic2['raceName'], dic2['Circuit']['circuitId'], dic2['date']]
    dic3 = dic2['Results']

    # segundo nó
    for j in range(len(dic3)):
      dic3 = dic2['Results'][j]
      
      # quando não existe 'position' no dicionario (valor position nulo)
      if 'position' not in dic3:
        position = ''
      else:
        position = dic3['position']
      # quando não existe 'Time' no dicionario (valor time nulo)
      if 'Time' not in dic3:
        millis = ''
        time = ''
      else:
        millis = dic3['Time']['millis']
        time = dic3['Time']['time']

      # adicionando valores do segundo nó do dicionário à lista 
      # tranformando a lista em dataframe para poder transpor (com formato linha)       
      dados_race2 = [position, dic3['points'], dic3['Driver']['driverId'], 
                      dic3['Constructor']['constructorId'], dic3['grid'], dic3['laps'], 
                      dic3['status'], millis, time]
      dados_race = dados_race1 + dados_race2
      df = pd.DataFrame(dados_race).transpose()

      # renomeando as colunas do 'data'
      df = df.rename(columns={0:'season', 1:'raceName', 2:'circuitRef', 3:'date', 4:'position', 
                              5:'points', 6:'driverRef', 7:'construtor', 8:'grid', 9:'laps', 
                              10:'status',11:'millis', 12:'time'}, 
                                        inplace=False)     
      df_final = df_final.append(df, ignore_index=True)
      j=+ 1
    i =+ 1
  df_final.to_csv(r'D:\Cursos-Maratonas-Bootcamps\Gama Academy\Projeto\resultados.csv')