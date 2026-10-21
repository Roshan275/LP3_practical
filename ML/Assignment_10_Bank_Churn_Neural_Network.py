"""Assignment 10: feed-forward neural network for bank customer churn.

PRACTICAL RUN / INPUTS
1. Install packages once: python3 -m pip install -r requirements.txt
2. Download Bank Customer Churn Modeling CSV (commonly Churn_Modelling.csv).
3. Run: python3 Assignment_10_Bank_Churn_Neural_Network.py
4. Enter the CSV path. It must include the target column Exited (0/1).
Prints test accuracy and a confusion matrix. Uses an improved MLP with two
hidden layers, early stopping, one-hot encoding, and normalized numeric inputs.
"""

from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main():
    csv_path = input("Path to bank churn CSV: ").strip().strip('"')
    path = Path(csv_path).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"Could not find {path}. Download the CSV and enter its correct path.")
    data = pd.read_csv(path)
    if "Exited" not in data.columns:
        raise ValueError("Could not find target column 'Exited'. Check that this is the Bank Churn dataset.")

    y = pd.to_numeric(data["Exited"], errors="coerce")
    X = data.drop(columns=["Exited"])
    # These are row/customer identifiers, not useful signals for predicting churn.
    X = X.drop(columns=[column for column in ("RowNumber", "CustomerId", "Surname") if column in X.columns])
    valid = y.isin([0, 1])
    X, y = X.loc[valid], y.loc[valid].astype(int)
    numeric_columns = X.select_dtypes(include="number").columns.tolist()
    categorical_columns = [column for column in X.columns if column not in numeric_columns]
    if not numeric_columns and not categorical_columns:
        raise ValueError("No usable feature columns were found.")

    numeric_pipeline = Pipeline([("fill", SimpleImputer(strategy="median")), ("scale", StandardScaler())])
    categorical_pipeline = Pipeline([
        ("fill", SimpleImputer(strategy="most_frequent")),
        ("one_hot", OneHotEncoder(handle_unknown="ignore")),
    ])
    preprocessing = ColumnTransformer([
        ("numeric", numeric_pipeline, numeric_columns),
        ("categorical", categorical_pipeline, categorical_columns),
    ])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model = Pipeline([
        ("preprocess", preprocessing),
        ("neural_network", MLPClassifier(
            hidden_layer_sizes=(32, 16), activation="relu", solver="adam",
            learning_rate_init=0.001, max_iter=300, early_stopping=True,
            validation_fraction=0.15, random_state=42,
        )),
    ])
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    print(f"Rows used: {len(X)}")
    print(f"Accuracy: {accuracy_score(y_test, prediction):.4f}")
    print("Confusion matrix (rows=true [0,1], columns=predicted [0,1]):")
    print(confusion_matrix(y_test, prediction, labels=[0, 1]))
    print("\nClassification report:")
    print(classification_report(y_test, prediction, zero_division=0))


if __name__ == "__main__":
    main()
