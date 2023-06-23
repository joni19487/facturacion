import pandas as pd
import claves_fiscales


df = pd.read_csv("BAGNAT.csv", encoding="latin-1")

for row,datos in df.iterrows():
    tipo=str(datos['TIPO'])
    descripcion=str(datos['DESCRIPCION'])
    cuit_receptor=str(datos['CUIT RECEPTOR'])
    fecha=str(datos['FECHA'])
    importe=str(datos['IMPORTE'])
    condicion=str(datos['CONDICION'])
    

