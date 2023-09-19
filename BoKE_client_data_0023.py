import pandas as pd
import numpy as np
import json
#EXTRACT

CSV_file = 'BOKHEM_clientData.csv'
df = pd.read_csv(CSV_file)
print(df)

#TRANSFORM

df=df.dropna(axis=0, how='any') #cut-off the rows with NaN values
df=df.drop_duplicates()#cut-off all duplicates

#LOAD

print(df.to_json(orient='split', indent=2))

json_storage=df.to_json('BoKE_clients_updated.json',orient='records', lines='True')

with open('BoKE_clients_updated.json','r') as f:
    data = json.load(f)
print(data)
