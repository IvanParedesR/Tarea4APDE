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

## Con el modelo antes calculado, aquí le pedimos al usuario que señale sus valores esperados para cada variable.
numero1 = float(input(f"Del 1 al 10 en que tan buena condición esperas que este la casa, siendo 1 mala y 10 excelente: "))
numero2 = float(input(f"De qué tamaño esperas que sea el terreno en pies cuadrados: "))
numero3 = float(input(f"Cuántos lugares de estacionamiento quieres: "))
numero4 = float(input(f"Año de su última renovación en 4 cifras: "))

# Realizamos el cálculo
resultado = -8.485e+05 + (numero1 * 2.989e+04) + (numero2 * 1.1699) + (numero3 * 2.29e+04) + (numero4 * 399.0900)

# Imprimimos el resultado
print(f"El precio aproximado de una casa con esas caracteristicas es: {int(resultado)}")
