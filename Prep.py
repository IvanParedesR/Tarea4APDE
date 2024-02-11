# Cargamos librerías, en general agregamos su documentación para futura consulta, salvo por pandas que es de uso más común.
import pandas as pd
import seaborn as sns #https://seaborn.pydata.org/installing.html
import statsmodels.api as smf #https://www.statsmodels.org/v0.10.2/importpaths.html
import statsmodels.formula.api as smq
import statsmodels.regression.linear_model as sm
from sklearn.model_selection import train_test_split #https://scikit-learn.org/stable/
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt #https://matplotlib.org/2.0.2/users/pyplot_tutorial.html

# Cargar el dataset de entrenamiento que se encuentra en el mismo lugar de 
df_training = pd.read_csv('train.csv')