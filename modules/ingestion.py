import pandas as pd
import numpy as np
from config import DATA_PATH

def inject_issues(df):
    df_copy = df.copy()

    for col in df_copy.columns:
        df_copy.loc[df_copy.sample(frac=0.05).index, col] = np.nan

    df_copy = pd.concat([df_copy, df_copy.sample(frac=0.05)])

    return df_copy

def load_data():
    df = pd.read_csv(DATA_PATH)
    df = inject_issues(df)
    return df