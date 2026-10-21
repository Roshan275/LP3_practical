"""Assignment 9: classify email as spam (1) or not spam (0).

PRACTICAL RUN / INPUTS
1. Install packages once: python3 -m pip install -r requirements.txt
2. Download the Email Spam Classification CSV from the assignment link.
3. Run: python3 Assignment_9_Email_Spam_Classification.py
4. Enter the CSV path. Expected format: first column is an email/name ID,
   last column is the 0/1 spam label, and intervening columns are word counts.
Prints accuracy, confusion matrix, precision, recall, and F1 for KNN and SVM.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC


def main():
    csv_path = input("Path to email spam CSV: ").strip().strip('"')
    path = Path(csv_path).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"Could not find {path}. Download the CSV and enter its correct path.")
    data = pd.read_csv(path)
    if data.shape[1] < 3:
        raise ValueError("Expected an ID column, feature columns, and a target column.")

    # This dataset's documented format has an identifier first and label last.
    X = data.iloc[:, 1:-1].apply(pd.to_numeric, errors="coerce")
    y = pd.to_numeric(data.iloc[:, -1], errors="coerce")
    valid_rows = y.isin([0, 1])
    X, y = X.loc[valid_rows], y.loc[valid_rows].astype(int)
    X = X.replace([np.inf, -np.inf], np.nan).fillna(0)
    if y.nunique() != 2:
        raise ValueError("The last CSV column should contain both spam labels 0 and 1.")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    # The PDF calls for SVM; a linear SVM is a practical choice for 3,000 features.
    models = {
        "K-Nearest Neighbors (k=5)": make_pipeline(
            StandardScaler(), KNeighborsClassifier(n_neighbors=5, n_jobs=-1)
        ),
        "Support Vector Machine (linear)": make_pipeline(
            StandardScaler(), LinearSVC(random_state=42, max_iter=5000)
        ),
    }
    print(f"Rows: {len(data)}; word-count features: {X.shape[1]}")
    for name, model in models.items():
        model.fit(X_train, y_train)
        prediction = model.predict(X_test)
        print(f"\n{name}")
        print("  Confusion matrix (rows=true [0,1], columns=predicted [0,1]):")
        print(confusion_matrix(y_test, prediction, labels=[0, 1]))
        print(f"  Accuracy:  {accuracy_score(y_test, prediction):.4f}")
        print(f"  Precision: {precision_score(y_test, prediction, zero_division=0):.4f}")
        print(f"  Recall:    {recall_score(y_test, prediction, zero_division=0):.4f}")
        print(f"  F1:        {f1_score(y_test, prediction, zero_division=0):.4f}")


if __name__ == "__main__":
    main()
