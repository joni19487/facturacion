import pandas as pd

df = pd.read_csv("libro1.csv", encoding="latin-1")

for row, datos in df.iterrows():
    
    cuitreal=datos['CUIT']
    descripcion=datos['DESCRIPCION']
    cuit_receptor=datos['CUIT RECEPTOR']
    importe=datos['IMPORTE']

    print(importe)