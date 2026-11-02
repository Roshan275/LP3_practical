# ML Practical Assignments 8–12

The practical implementations are Jupyter notebooks. Open the matching notebook in Jupyter Notebook, JupyterLab, or VS Code, download its dataset, update the CSV path in the notebook if needed, then run the cells from top to bottom.

## Setup

From a terminal opened at the repository root:

```bash
python3 -m pip install -r ML/requirements.txt
python3 -m pip install notebook
python3 -m notebook
```

Alternatively, open a notebook file directly in VS Code with the Jupyter extension. Select the Python environment where the dependencies were installed.

## Notebooks and datasets

| Assignment | Notebook | Dataset expected |
|---|---|---|
| 8 — Uber fare prediction | `uber.ipynb` | Uber Fares CSV, commonly `uber.csv`, with fare and pickup/drop-off coordinates. |
| 9 — Email spam classification | `email.ipynb` | Email spam CSV with email identifier, word-count features, and a 0/1 spam label. |
| 10 — Bank churn neural network | `churning.ipynb` | Bank Customer Churn CSV, commonly `Churn_Modelling.csv`, including the `Exited` target. TensorFlow is needed for this notebook. |
| 11 — Diabetes KNN classification | `diabetes.ipynb` | `diabetes.csv`, including numeric patient features and `Outcome` target. |
| 12 — Customer/sales clustering | `sales.ipynb` | The sales/customer CSV used by the notebook; verify its expected file name and columns in the first data-loading cells. |

Place each CSV where the notebook expects it, or change the `read_csv`/`read_excel` path in its data-loading cell. The exact dataset download source and column names can differ between copies; check the notebook's first few cells before running the full analysis.
