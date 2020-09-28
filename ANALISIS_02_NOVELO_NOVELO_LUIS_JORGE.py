
import pandas as pd

file = 'synergy_logistics_database.csv'


masterData = pd.read_csv(file)

expData = masterData.loc[masterData['direction'] == 'Exports']
impData = masterData.loc[masterData['direction'] == 'Imports']


topExpRout = expData.groupby(['origin','destination']).size().sort_values(ascending=False)

print('\n Top 10 rutas de exportación \n')
print(topExpRout.head(10))
print('\n')


topImpRout = impData.groupby(['origin','destination']).size().sort_values(ascending=False)
print('\n Top 10 rutas de importación \n')
print(topImpRout.head(10))
print('\n')



topExpTransport = expData.groupby(['transport_mode'])['total_value'].sum().reset_index().sort_values(['total_value'], ascending = False)
print('\n Top 3 medios de transporte en exportaciones por valor \n')
print(topExpTransport.head(3)) #tierra se descarta
print('\n')


topImpTransport = impData.groupby(['transport_mode'])['total_value'].sum().reset_index().sort_values(['total_value'], ascending = False)
print('\n Top 3 medios de transporte en importaciones por valor \n')
print(topImpTransport.head(3)) #aire se descarta
print('\n')



expByCountry = expData.groupby(['origin'])['total_value'].sum().reset_index().sort_values(['total_value'], ascending = False)

n = 80 #Definición del porcentaje
print('\n 80% del valor total de exportaciones por pais \n')
print(expByCountry.head(int(len(expByCountry)*(n/100))))
print('\n')



impByCountry = impData.groupby(['origin'])['total_value'].sum().reset_index().sort_values(['total_value'], ascending = False)

print('\n 80% del valor total de importaciones por pais \n')
print(impByCountry.head(int(len(impByCountry)*(n/100))))
print('\n')





