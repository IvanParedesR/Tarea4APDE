# Cargamos librerías, en general agregamos su documentación para futura consulta, salvo por pandas que es de uso más común.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt #https://matplotlib.org/2.0.2/users/pyplot_tutorial.html


# Cargar el dataset de entrenamiento que se encuentra en el mismo lugar de 
df_training = pd.read_csv('02Data/train.csv')

# Ver el tamaño del set
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

# Catalogamos las 10 caracteristicas principales
top15corrcaracteri = df_corr.corr()['SalePrice']
top15corrcaracteri = top15corrcaracteri[:15]
print(top15corrcaracteri)