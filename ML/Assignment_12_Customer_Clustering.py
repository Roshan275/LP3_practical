"""Assignment 12: customer/sales clustering and the elbow method.

PRACTICAL RUN / INPUTS
1. Install packages once: python3 -m pip install -r requirements.txt
2. Download sales_data_sample.csv, or use a Mall Customers CSV.
3. Run: python3 Assignment_12_Customer_Clustering.py
4. Enter the CSV path, then enter a cluster count (5 is a common Mall Customers
   example; use the elbow graph to choose the value appropriate for your data).
The script prints WCSS values, saves elbow_plot.png and clustered_data.csv, and
also runs hierarchical clustering for comparison. It prefers Age, Annual Income,
and Spending Score columns when available; otherwise uses numeric columns.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.preprocessing import StandardScaler


def choose_features(data):
    """Prefer the practical's customer attributes, else use usable numeric data."""
    normalized = {column.lower().strip(): column for column in data.columns}
    preferred_groups = [
        ("age",),
        ("annual income (k$)", "annual income", "annual_income"),
        ("spending score (1-100)", "spending score", "spending_score"),
    ]
    selected = []
    for choices in preferred_groups:
        match = next((normalized[name] for name in choices if name in normalized), None)
        if match is not None:
            selected.append(match)
    if len(selected) >= 2:
        return data[selected].apply(pd.to_numeric, errors="coerce"), selected

    numeric = data.select_dtypes(include="number")
    # Avoid treating a likely row/customer/order identifier as a meaningful distance.
    remove = [c for c in numeric.columns if c.lower().strip() in {
        "id", "customerid", "customer_id", "ordernumber", "orderlinenumber", "rownumber"
    }]
    numeric = numeric.drop(columns=remove, errors="ignore")
    if numeric.shape[1] < 2:
        raise ValueError("Need at least two numeric feature columns for clustering.")
    return numeric, list(numeric.columns)


def main():
    csv_path = input("Path to sales/customer CSV: ").strip().strip('"')
    path = Path(csv_path).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"Could not find {path}. Download the dataset and enter its correct path.")
    data = pd.read_csv(path)
    features, feature_names = choose_features(data)
    features = features.replace([np.inf, -np.inf], np.nan)
    valid_rows = features.notna().all(axis=1)
    cleaned = data.loc[valid_rows].copy()
    features = features.loc[valid_rows]
    if len(features) < 3:
        raise ValueError("At least three complete customer rows are needed.")

    scaled = StandardScaler().fit_transform(features)
    max_k = min(10, len(features) - 1)
    k_values = list(range(1, max_k + 1))
    wcss = []
    for k in k_values:
        estimator = KMeans(n_clusters=k, random_state=42, n_init=10)
        estimator.fit(scaled)
        wcss.append(estimator.inertia_)

    plt.plot(k_values, wcss, marker="o")
    plt.xticks(k_values)
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("WCSS / inertia")
    plt.title("Elbow Method")
    plt.tight_layout()
    plot_path = Path("elbow_plot.png")
    plt.savefig(plot_path, dpi=150)
    plt.close()

    print("Features used:", ", ".join(map(str, feature_names)))
    print("Elbow values (k: WCSS):")
    for k, score in zip(k_values, wcss):
        print(f"  {k}: {score:.2f}")
    print(f"Elbow graph saved to: {plot_path.resolve()}")
    cluster_count = int(input(f"Choose k from the graph (1-{max_k}; default 5): ") or "5")
    if not 1 <= cluster_count <= max_k:
        raise ValueError(f"Choose a cluster count between 1 and {max_k}.")

    kmeans = KMeans(n_clusters=cluster_count, random_state=42, n_init=10)
    cleaned["KMeans_Cluster"] = kmeans.fit_predict(scaled)
    if cluster_count >= 2:
        hierarchical = AgglomerativeClustering(n_clusters=cluster_count)
        cleaned["Hierarchical_Cluster"] = hierarchical.fit_predict(scaled)
    output_path = Path("clustered_data.csv")
    cleaned.to_csv(output_path, index=False)
    print("\nK-Means cluster sizes:")
    print(cleaned["KMeans_Cluster"].value_counts().sort_index().to_string())
    print(f"Cluster-labeled data saved to: {output_path.resolve()}")
    print("StandardScaler was used because the numeric features may have different units.")


if __name__ == "__main__":
    main()
