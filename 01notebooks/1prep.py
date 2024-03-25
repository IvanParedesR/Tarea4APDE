# Cargamos librerías, en general agregamos su documentación para futura consulta.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt #https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
import statsmodels.api as smf #https://www.statsmodels.org/v0.10.2/importpaths.html

#Cargar el dataset de entrenamiento que se encuentra en el mismo lugar de 
#def load_data(file_path):
#    try:
#       df_training=pd.read_csv(file_path)
#        return df.head(5)
#    except FileNotFoundError:
#        print(f"El archivo no está en este path: {file_path}")
#        print(f"Busca en otro lugar, por lo pronto no podemos proceder.")

df_training=pd.read_csv('02Data/train.csv')
#Ver el tamaño del set
print("train size:",df_training.shape)
# El resultado es: train size: (1460, 81)
#Vemos las 10 primeras observaciones y las variables numericas.
df_training.describe()
#Información de los tipos de variable, hay bastantes que son objeto.
df_training.info()
# Describimos la variable dependiente de precio de venta y 
print(df_training['SalePrice'].describe())
#Graficamos su histograma
plt.figure(figsize=(9, 5)) # Establecemos tamaño
sns.displot(df_training['SalePrice'], color='r', bins=50, kde=True, alpha=0.4)
plt.show()
# Eliminamos los datos que no son numericos y creamos un mapa de calor con la relación entre las distintas variables.
df_corr = df_training.astype("float64",errors='ignore')
df_corr = df_corr.select_dtypes(exclude="object")
plt.subplots(figsize=(12,9))
sns.heatmap(df_corr.corr())
plt.show()

# Catalogamos las 10 caracteristicas principales
top15corrcaracteri = df_corr.corr()['SalePrice']
top15corrcaracteri = top15corrcaracteri[:15]
print(top15corrcaracteri)
# Realizamos planos de scatter con variables relevates antes calculadas 
plt.title("Scatter de 'SalePrice'vs '1stFlrSF'")
plt.scatter(x=df_training['1stFlrSF'], y=df_training['SalePrice'])
plt.plot()
<<<<<<< HEAD:01notebooks/Prep.py
plt.show()

=======
>>>>>>> e4ab4a2bf4358bb003ccf4f8709c27c71a266f7a:01notebooks/1prep.py
# Realizamos planos de scatter con variables relevates antes calculadas 
plt.title("Scatter de 'SalePrice'vs 'OverallQual'")
plt.scatter(x=df_training['OverallQual'], y=df_training['SalePrice'])
plt.plot()
<<<<<<< HEAD:01notebooks/Prep.py
plt.show()

=======
>>>>>>> e4ab4a2bf4358bb003ccf4f8709c27c71a266f7a:01notebooks/1prep.py
# Realizamos planos de scatter con variables relevates antes calculadas 
plt.title("Scatter de 'SalePrice'vs 'TotalBsmtSF'")
plt.scatter(x=df_training['TotalBsmtSF'], y=df_training['SalePrice'])
plt.plot()
#elminamos los valores extremos, la segmentacion se debe a que en el histograma 
#esos valores son pocos y están por encima del 95% de la muestra
df_corr.drop(df_corr[(df_corr['SalePrice']>450000)].index, inplace=True)
#Observamos el nuevo tamaño de la base, se perdieron menos de 14 valores
#el 0.001% de la base
print("train size:",df_corr.shape)
#Preparamos los datos de la regresión, agregamos una constante
X=df_corr[['OverallQual','LotArea','GrLivArea','GarageCars','YearBuilt','YearRemodAdd','MSSubClass','1stFlrSF','TotalBsmtSF']]  # Cambia 'tu_variable_independiente' por el nombre de tu columna
y=df_corr['SalePrice'] 
X=smf.add_constant(X)
#Guardamos datos procesado
df_corr.to_csv('02Data/dataprocesada.csv', index=False)