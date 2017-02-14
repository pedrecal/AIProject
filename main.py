#import pandas as pd
#df_size = 3006
#df_headers = ['Energia', 'Contraste', 'Correlacao', 'Variancia', 'MDI', 'Media Soma', 'Variancia Soma',
#              'Entropia Soma', 'Entropia', 'Variancia Diferenca', 'Entropia Diferenca', 'Medidas Correlacao 1',
#              'Medidas Correlacao 2']
#df = pd.read_csv('new_data.csv', names=df_headers)
# print(df.head())

#df2 = pd.read_csv('labels.csv', header=None)
#df2.columns = ['Diagnostico']
# print(df2.head())


#df2['Diagnostico'][df2['Diagnostico'] == 'Normal'] = 0
#df2['Diagnostico'][df2['Diagnostico'] == 'Cancer'] = 1
#df2['Diagnostico'][df2['Diagnostico'] == 'Benigno'] = 2
# print(df2.head())

#df['Diagnostico'] = df2['Diagnostico']
# print(df)

#df.to_csv('data_with_diagnosis.csv')

#Contraste, Correlacao e Variancaia
#Correlacao2

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_with_diagnosis.csv')
print(df.head(10))
x = df['Diagnostico']
y = df['Variancia']

plt.scatter(x,y)
plt.show()
