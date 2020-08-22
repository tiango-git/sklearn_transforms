from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

 # Trasnformación para estandarizar los datos
class Scaler(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.sc = StandardScaler()

    def fit(self, X, y=None):
        data = X.copy()
        self.sc.fit_transform(data)
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        x_tmp = X.copy()
        data = self.sc.transform(x_tmp)
        data = pd.DataFrame.from_records(data=data, columns=x_tmp.columns)
        return data
