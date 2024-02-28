import seaborn as sns
#import statsmodels.api as smf #https://www.statsmodels.org/v0.10.2/importpaths.html
#import statsmodels.formula.api as smq
#import statsmodels.regression.linear_model as sm
#from sklearn.model_selection import train_test_split #https://scikit-learn.org/stable/
#from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt #https://matplotlib.org/2.0.2/users/pyplot_tutorial.html


#Vemos las 10 primeras observaciones y las variables numericas.
df_training.describe()

#Información de los tipos de variable, hay bastantes que son objeto.
df_training.info()

#Describimos la variable dependiente de precio de venta 
print(df_training['SalePrice'].describe())

#Graficamos su histograma
plt.figure(figsize=(9, 5)) # Establecemos tamaño
sns.distplot(df_training['SalePrice'], color='r', bins=50, hist_kws={'alpha': 0.4})

#Eliminamos los datos que no son numericos y creamos un mapa de calor 
#con la relación entre las distintas variables.
df_corr = df_training.astype("float64",errors='ignore')
df_corr = df_corr.select_dtypes(exclude="object")
plt.subplots(figsize=(12,9))
sns.heatmap(df_corr.corr())