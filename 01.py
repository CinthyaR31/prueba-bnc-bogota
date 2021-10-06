"""
1.  Escribir un programa que lea un archivo que contiene los n millones de votos otorgados a los
candidatos A, B y C a la presidencia e imprimir el candidato, la cantidad de votos  y el porcentaje
de votación para cada uno.
"""
# Imports
import pandas as pd

# Reading File
file_votes = pd.read_csv('./files/data.csv', sep=';')

# Solution
result_group = file_votes.groupby(['TIPO', 'CANDIDATO']).agg({'VOTO': 'sum'})
result_group['percentage'] = result_group.groupby(level=0).apply(lambda x:
                                                                 100 * x / float(x.sum()))
print(result_group)
