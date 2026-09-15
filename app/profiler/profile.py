import pandas as pd

def load_excel(file_path: str) -> pd.DataFrame:
    return pd.read_excel(file_path)

def profile_dataframe(df: pd.DataFrame) -> dict:
    profile = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns":{}
    }

    for column in df.columns:
        profile["columns"][column]={
            "data_type": str(df[column].dtype),
            "missing_count": int(df[column].isna().sum()),
            "unique_count": int(df[column].nunique()),
            "sample_values": df[column].dropna().head(5).tolist()
        }
    return profile
