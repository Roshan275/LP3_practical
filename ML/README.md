# ML Practical Assignments 8–12

Each assignment has its own Python file. Download the relevant CSV dataset first, then run its file from Terminal. The programs ask for the CSV path; you can type a full path or a path relative to the current folder.

## Setup

Use Python 3. Install the packages once:

```bash
cd "/Users/rjamsandekar/Desktop/College/Fun/ML"
python3 -m pip install -r requirements.txt
```

Run an assignment with `python3 <filename>.py`. Each program prints its required results; Assignment 12 also saves an elbow plot image and a CSV containing cluster labels.

## Assignments and datasets

1. **Assignment 8 — Uber fare regression**: download the Uber Fares dataset CSV (commonly named `uber.csv`). It should include `fare_amount`, pickup/dropoff latitude and longitude, and usually `pickup_datetime` and `passenger_count`.
2. **Assignment 9 — Email spam classification**: download the Email Spam Classification CSV. It should have an email/name identifier in the first column, word-count features, and the spam label (0/1) in the last column.
3. **Assignment 10 — Bank customer churn neural network**: download the Bank Customer Churn Modeling CSV (commonly `Churn_Modelling.csv`). It should have an `Exited` target column and customer attributes such as Geography, Gender, Age, Balance, etc.
4. **Assignment 11 — Diabetes KNN**: download `diabetes.csv` with numeric patient features and an `Outcome` target column (0/1).
5. **Assignment 12 — Customer/sales clustering**: provide `sales_data_sample.csv` or the Mall Customers CSV. For Mall Customers, the program uses Age, Annual Income, and Spending Score when present. For other sales data, it selects and scales usable numeric columns.

If a CSV is in the ML folder, enter just its filename at the prompt. Otherwise enter the full path, for example `/Users/yourname/Downloads/uber.csv`.
