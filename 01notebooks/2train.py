# Cargamos librerías, en general agregamos su documentación para futura consulta.
import pandas as pd
import statsmodels.regression.linear_model as sm
import statsmodels.api as smf #https://www.statsmodels.org/v0.10.2/importpaths.html

#Cargar el dataset de entrenamiento que se encuentra en el mismo lugar de 
df_procesado=pd.read_csv('02Data/dataprocesada.csv')

# Preparamos los datos de la regresión corrigiendo lo que señalamos en la línea previa
X = df_procesado[['OverallQual','LotArea','GarageCars','YearRemodAdd','MSSubClass','TotalBsmtSF']]  # Cambia 'tu_variable_independiente' por el nombre de tu columna
y = df_procesado['SalePrice'] 
X = smf.add_constant(X)
model = sm.OLS(y,X)
fitted_model = model.fit()
fitted_model.summary()

#Vemos las 10 primeras observaciones y las variables numericas.
df_procesado.describe()

X_test = df_procesado[['OverallQual','LotArea','GarageCars','YearRemodAdd','MSSubClass','TotalBsmtSF']]
X_test = smf.add_constant(X_test)
df_procesado.describe()
