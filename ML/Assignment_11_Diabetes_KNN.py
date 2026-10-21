"""Assignment 11: KNN diabetes classification and evaluation metrics.

PRACTICAL RUN / INPUTS
1. Install packages once: python3 -m pip install -r requirements.txt
2. Download diabetes.csv (Pima Indians Diabetes dataset).
3. Run: python3 Assignment_11_Diabetes_KNN.py
4. Enter the CSV path. The target column should be named Outcome and contain 0/1.
Prints confusion matrix, accuracy, error rate, precision, and recall.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main():
    csv_path = input("Path to diabetes.csv: ").strip().strip('"')
    path = Path(csv_path).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"Could not find {path}. Download diabetes.csv and enter its correct path.")
    data = pd.read_csv(path)
    if "Outcome" not in data.columns:
        raise ValueError("Could not find target column 'Outcome'. Check the diabetes CSV format.")

    y = pd.to_numeric(data["Outcome"], errors="coerce")
    X = data.drop(columns=["Outcome"]).apply(pd.to_numeric, errors="coerce")
    valid = y.isin([0, 1])
    X, y = X.loc[valid], y.loc[valid].astype(int)

    # In this dataset zero often means a missing clinical measurement for these fields.
    for column in ("Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"):
        if column in X:
            X[column] = X[column].replace(0, np.nan)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y
    )
    model = make_pipeline(
        SimpleImputer(strategy="median"),
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=3),
    )
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    accuracy = accuracy_score(y_test, prediction)
    print(f"Rows used: {len(X)}; features: {X.shape[1]}")
    print("Confusion matrix (rows=true [0,1], columns=predicted [0,1]):")
    print(confusion_matrix(y_test, prediction, labels=[0, 1]))
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Error rate:{1 - accuracy: .4f}")
    print(f"Precision: {precision_score(y_test, prediction, zero_division=0):.4f}")
    print(f"Recall:    {recall_score(y_test, prediction, zero_division=0):.4f}")


if __name__ == "__main__":
    main()
