"""Assignment 8: preprocess Uber ride data and compare regression models.

PRACTICAL RUN / INPUTS
1. Install packages once: python3 -m pip install -r requirements.txt
2. Download the Uber Fares dataset CSV (often uber.csv).
3. Run: python3 Assignment_8_Uber_Fare_Regression.py
4. Enter the CSV filename/path when prompted (for example: uber.csv).
   Expected fields include fare_amount and pickup/dropoff latitude/longitude.
   pickup_datetime and passenger_count are used when available.
The program prints R2, RMSE, and MAE for Linear Regression and Random Forest.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def haversine_km(lat1, lon1, lat2, lon2):
    """Calculate straight-line distance over the earth in kilometers."""
    earth_radius_km = 6371.0
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    value = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    return 2 * earth_radius_km * np.arcsin(np.sqrt(value))


def main():
    csv_path = input("Path to Uber fares CSV (e.g. uber.csv): ").strip().strip('"')
    path = Path(csv_path).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"Could not find {path}. Download the dataset and enter its correct path.")

    data = pd.read_csv(path)
    data.columns = [column.strip().lower() for column in data.columns]
    required = {"fare_amount", "pickup_latitude", "pickup_longitude", "dropoff_latitude", "dropoff_longitude"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError("CSV is missing required columns: " + ", ".join(sorted(missing)))

    data = data.replace([np.inf, -np.inf], np.nan).dropna(subset=list(required)).copy()
    data = data[(data.fare_amount > 0) & (data.fare_amount <= 500)]
    valid_geo = (
        data.pickup_latitude.between(-90, 90)
        & data.dropoff_latitude.between(-90, 90)
        & data.pickup_longitude.between(-180, 180)
        & data.dropoff_longitude.between(-180, 180)
    )
    data = data[valid_geo].copy()
    data["distance_km"] = haversine_km(
        data.pickup_latitude, data.pickup_longitude,
        data.dropoff_latitude, data.dropoff_longitude,
    )
    data = data[data.distance_km <= 200]
    if "pickup_datetime" in data:
        pickup_time = pd.to_datetime(data.pickup_datetime, errors="coerce", utc=True)
        data["pickup_hour"] = pickup_time.dt.hour
        data["pickup_day"] = pickup_time.dt.dayofweek
        data = data.dropna(subset=["pickup_hour", "pickup_day"])

    feature_columns = ["pickup_latitude", "pickup_longitude", "dropoff_latitude", "dropoff_longitude", "distance_km"]
    if "passenger_count" in data:
        data = data[data.passenger_count.between(1, 6)]
        feature_columns.append("passenger_count")
    for time_feature in ("pickup_hour", "pickup_day"):
        if time_feature in data:
            feature_columns.append(time_feature)
    data = data.replace([np.inf, -np.inf], np.nan).dropna(subset=feature_columns + ["fare_amount"])

    # Keep a practical runtime on very large copies of the Kaggle dataset.
    if len(data) > 100_000:
        data = data.sample(100_000, random_state=42)
    if len(data) < 20:
        raise ValueError("Too few valid rows remain after cleaning; check the CSV contents.")

    X, y = data[feature_columns], data.fare_amount
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    models = {
        "Linear Regression": make_pipeline(StandardScaler(), LinearRegression()),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1, min_samples_leaf=2),
    }
    print(f"Rows used after preprocessing: {len(data)}")
    print("Features:", ", ".join(feature_columns))
    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        print(f"\n{name}")
        print(f"  R2:   {r2_score(y_test, predictions):.4f}")
        print(f"  RMSE: {rmse:.4f}")
        print(f"  MAE:  {mean_absolute_error(y_test, predictions):.4f}")


if __name__ == "__main__":
    main()
