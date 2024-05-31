from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import Parallel, delayed

# Función para evaluar un modelo de RandomForestClassifier con un número específico de árboles (n_estimators)
def evaluate_model(n_estimators, X_train, X_test, y_train, y_test):
    # Crear el modelo con el número especificado de árboles
    model = RandomForestClassifier(n_estimators=n_estimators)
    # Entrenar el modelo con los datos de entrenamiento
    model.fit(X_train, y_train)
    # Predecir las etiquetas para los datos de prueba
    y_pred = model.predict(X_test)
    # Calcular y retornar la precisión del modelo
    return (n_estimators, accuracy_score(y_test, y_pred))

# Función para evaluar varios modelos en paralelo
def parallel_model_evaluation():
    # Cargar el conjunto de datos Iris
    iris = load_iris()
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)
    # Lista de valores de n_estimators a evaluar
    n_estimators_list = [10, 50, 100, 200]
    # Evaluar los modelos en paralelo usando joblib.Parallel y joblib.delayed
    results = Parallel(n_jobs=4)(delayed(evaluate_model)(n, X_train, X_test, y_train, y_test) for n in n_estimators_list)
    # Retornar los resultados
    return results

# Ejecutar la evaluación de modelos en paralelo
results = parallel_model_evaluation()
# Imprimir los resultados
print(results)
