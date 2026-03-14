"""
Datasets tratados em Parquet.

Os arquivos são gerados pelo notebook 01_load_datasets.ipynb e salvos em:
  data/processed/
    - accounts.parquet
    - subscriptions.parquet
    - feature_usage.parquet
    - support_tickets.parquet
    - churn_events.parquet
"""

from pathlib import Path

import pandas as pd

PROCESSED_DIR = Path(__file__).resolve().parent / "processed"


def load_processed(name: str) -> pd.DataFrame:
    """Carrega um dataset tratado por nome: accounts, subscriptions, feature_usage, support_tickets, churn_events."""
    path = PROCESSED_DIR / f"{name}.parquet"
    if not path.exists():
        raise FileNotFoundError(f"Execute o notebook 01_load_datasets.ipynb para gerar {path}")
    return pd.read_parquet(path)
