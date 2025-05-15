import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("votaciones2006/Computos2006-Presidente.txt", sep='|')
print("Numero entradas:", data.shape)
st.markdown("# Análisis de datos de las votaciones del 2006")
st.markdown("Primero cargamos los datos")
st.markdown("Número entradas {data.shape}")

idstate = {1: 'Aguascalientes', 2:'Baja California', 3: 'Baja California Sur', 4: 'Campeche',
           5: 'Coahuila', 6: 'Colima', 7: 'Chiapas', 8: 'Chihuahua', 9:'CDMX', 10: 'Durango',
           11: 'Guanajuato', 12: 'Guerrero', 13: 'Hidalgo', 14: 'Jalisco', 15: 'México',
           16: 'Michoacán', 17: 'Morelos', 18: 'Nayarit', 19: 'Nuevo León', 20: 'Oaxaca',
           21: 'Puebla', 22: 'Querétaro', 23: 'Quintana Roo', 24: 'San Luis Potosí',
           25: 'Sinaloa', 26: 'Sonora', 27: 'Tabasco', 28: 'Tamaulipas', 29: 'Tlaxcala',
           30: 'Veracruz', 31: 'Yucatán', 32: 'Zacatecas'} 

data['ID_ESTADO'] = data['ID_ESTADO'].apply(lambda x: idstate[x] )
datos_10 = data.head(10)
print(datos_10['ID_ESTADO'])
st.table(datos_10['ID_ESTADO'])
data.rename(columns = {'ID_ESTADO': 'ESTADO'}, inplace = True)
len(data.ESTADO.unique())
st.markdown(f"Los estados que votaron son::{len(data.ESTADO.unique())}")


voto_extranjero = data[data['TIPO_CANDIDATURA'] == 6]
voto_local = data[data['TIPO_CANDIDATURA'] == 1] 
voto_extranjero = voto_extranjero.drop(columns = ["TIPO_CANDIDATURA"])
voto_local = voto_local.drop(columns = ["TIPO_CANDIDATURA"] )

st.markdown(f"## Análisis de los votos por candidato")
voto_local["PAN"].sum()

partidos = ["PAN", "PBT", "APM", "NA", "ASDC", "NO_VOTOS_VALIDOS", "NO_VOTOS_NULOS"]

suma_votos = voto_local[partidos].sum() + voto_extranjero[partidos].sum()
porcentaje_votos = suma_votos / suma_votos.sum() * 100

plt.figure(figsize=(10, 5))
plt.bar(porcentaje_votos.index, porcentaje_votos.values)
plt.xlabel('Partidos')

st.bar_chart(porcentaje_votos)

