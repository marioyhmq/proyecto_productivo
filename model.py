from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def entrenar_modelo(df):
    X = df[["EDAD", "SALDO_TOTAL_TARJETA", "CUPO_PROMEDIO_TARJETA",
            "ANTIGUEDAD_TARJETA_ANIOS", "INSTRUCCION"]]
    y = df["MORA"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = RandomForestClassifier()
    modelo.fit(X_train, y_train)
    return modelo, X_test, y_test

def evaluar_modelo(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    return classification_report(y_test, y_pred)
