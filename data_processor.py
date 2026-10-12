 #data_processor.py
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def remove_duplicates(df):
    """Remove duplicate rows."""
    before = len(df)
    df = df.drop_duplicates()
    logger.debug(f"remove_duplicates: {before} to {len(df)} rows")
    return df

def handle_missing(df, axis="rows"):
    """Drop rows or columns containing missing values."""
    if axis == "rows":
        before = len(df)
        df = df.dropna()
        logger.debug(f"handle_missing: {before} to {len(df)} rows")
    elif axis == 'columns':
        before = len(df.columns)
        df = df.dropna(axis=1)
        logger.debug(f"handle_missing: {before} to {len(df.columns)} columns") 
    else: 
        logger.debug(f"Unsupported axis: {axis}")
        raise ValueError(f"Unsupported axis: {axis}")
    return df

def remove_outliers(df, columns, method, threshold):
    """Remove outliers from the specified numeric columns."""
    supported_methods = ["iqr", "zscore"]
    if method not in supported_methods: 
        logger.error(f"Unsupported methods:{method}")
        raise ValueError(f"Unsupported methods:{method}")
    for col in columns:
        if col not in df.columns: 
            logger.warning(f"Column not here: {col}")
        elif not pd.api.types.is_numeric_dtype(df[col]):
            logger.warning(f"column not numeric:{col}")
        else:
            before = len(df)
            if method == "iqr":
                q1 = df[col].quantile(0.25)
                q3 = df[col].quantile(0.75)
                iqr = q3-q1
                lower = q1 - threshold * iqr 
                upper = q3 + threshold * iqr
                df = df[(df[col] >= lower) & (df[col] <= upper)]
            else: 
                mean = df[col].mean()
                std =df[col].std()
                z_score = (df[col] - mean) / std 
                df = df[z_score.abs() <= threshold]
            logger.debug(f'{col}: method={method}, threshold {threshold}, removed = {before -len(df)}')
    return df 


def process_data(df, config):
    """Apply the processing steps enabled in the configuration."""
    settings = config["processing"]

    if settings["remove_duplicates"]:
        df = remove_duplicates(df)

    if settings["missing"]["enabled"]:
        df = handle_missing(df, settings["missing"]["axis"])

    if settings["outliers"]["enabled"]:
        df = remove_outliers(df, settings["outliers"]["columns"], settings["outliers"]["method"], settings["outliers"]["threshold"])
    return df 

        
      
    


def create_cleaning_report(df_before, df_after):
    """Return a dictionary summarizing the cleaning results."""
    report = {
        "rows_before": df_before.shape[0],
        "rows_after": df_after.shape[0],
        "rows_removed": df_before.shape[0] - df_after.shape[0],
        "columns_before": df_before.shape[1],
        "columns_after": df_after.shape[1],
        "columns_removed": df_before.shape[1] - df_after.shape[1],
    }
    return report