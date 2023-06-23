import pandas as pd
import funciones
corregidas=funciones.corrector()
df = pd.read_csv("corregidos.csv", encoding="latin-1")

for row, datos in df.iterrows():
    
    cuitreal=str(datos['CUIT'])
    descripcion=str(datos['DESCRIPCION'])
    cuit_receptor=str(datos['CUIT RECEPTOR'])
    importe=str(datos['IMPORTE'])

    print(cuitreal)
    

         
    

