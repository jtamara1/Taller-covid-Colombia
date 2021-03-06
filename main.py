"""jean tamara"""
import Casoscovid as pd
import matplotlib.pyplot as plt

url = 'Caso de covid'

data = pd.read_csv(url) 

data.drop('Código ISO del país', axis = 1, inplace=True)

data.drop('Nombre del país', axis = 1, inplace=True)

data.drop('Pertenencia étnica', axis = 1, inplace=True)

data.drop('Nombre del grupo étnico', axis = 1, inplace=True)

data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)

data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)


data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)

data['Sexo'].value_counts()
data.loc[data['Estado'] == 'leve'] = 'Leve'
data.loc[data['Estado'] == 'LEVE'] = 'Leve'

data.loc[data['Ubicación del caso'] == 'casa'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'CASA'] = 'Casa'
data.loc[data['Sexo'] == 'm'] =   'M'
data.loc[data['Sexo'] == 'f'] = 'F'

#Número de casos de Contagiados en el País.

data['Estado'].count()

#Número de Municipios Afectados

data['Nombre municipio'].nunique()

#Liste los municipios afectados (sin repetirlos)

data['Nombre municipio'].value_counts()

#Número de personas que se encuentran en atención en casa

aux = data.loc[(data['Ubicación del caso'] == 'Casa')]
NumeroDePersonasEnCasa = aux.shape[0]

#Número de personas que se encuentran recuperados

aux = data.loc[(data['Recuperado'] == 'Recuperado')]
NumeroDePersonasRecuper = aux.shape[0]

#Número de personas que ha fallecido

aux = data.loc[(data['Estado'] == 'Fallecido')]
NumeroDePersonasFallecidas = aux.shape[0]

#Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,Relacionado)
data.sort_values(by=data.loc[(data['Tipo de contagio'] == 'Importado')],ascending=False )


data.sort_values(by=data.loc[(data['Tipo de contagio'] == 'Relacionado')],ascending=False )

#Número de departamentos afectados
data['Nombre departamento'].nunique()

#Liste los departamentos afectados(sin repetirlos)
data['Sexo'].value_counts()

#Ordene de mayor a menor por tipo de atención
data.sort_values(by='Tipo de recuperación',ascending=False )

#Liste de mayor a menor los 10 departamentos con mas casos de contagiados
data['Nombre departamento'].value_counts().head(10)

#Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre departamento').size()

aux.sort_values(ascending=False).head(10)

#Liste de mayor a menor los 10 departamentos con mas casos de recuperados
aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre departamento').size()

aux.sort_values(ascending=False).head(10)

#Liste de mayor a menor los 10 municipios con mas casos de contagiados
data['Nombre municipio'].value_counts().head(10)

#Liste de mayor a menor los 10 municipios con mas casos de fallecidos
aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre municipio').size()

aux.sort_values(ascending=False).head(10)

#Liste de mayor a menor los 10 municipios con mas casos de recuperados
aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre municipio').size()

aux.sort_values(ascending=False).head(10)

#Liste agrupado por departamento y en orden de Mayor a menor las ciudades con mas casos de contagiados
aux = data.groupby(['Nombre departamento', 'Nombre municipio']).size()

aux.sort_values(ascending=False)

#Número de Mujeres y hombres contagiados por ciudad por departamento
aux = data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo']).size()

aux.sort_values(ascending=False)

#Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento
aux = data.groupby(['Nombre departamento', 'Nombre municipio', 'Edad']).size()

aux.sort_values(ascending=False)
