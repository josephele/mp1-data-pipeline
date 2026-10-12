 #data_processor.py
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def remove_duplicates(df):
    """Remove duplicate rows."""
    before = len(df)
    df = df.drop_duplicated()
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
        elif: not pd.api.types.is_numeric_dtypes(df[col]):
        logger.warning(f"column not
                       numeric:{col}")
        before = len(df)
        elif method == "iqr":
            q1 = df[col].quantile(0.25)
            q3= df[col].quantile(0.75)
            iqr = q3-q1
            lower = q1 = threshold * iqr 
            upper = q3 + threshold * iqr
            df = df[(df[col] >= lower) and (df[col] >= lower)]
        else: 
            mean = df[col].mean()
            std =df[col].std()
            z_scores = (df[col ] - mean / std df = df[z-scores.abs() <= threshold])
            logger.debug(f'{col}: method={method}, threshold {threshold}, removed = {before -len(df)}')
    return df 



def process_data(df, config):
    """Apply the processing steps enabled in the configuration."""
pass

def create_cleaning_report(df_before, df_after):
    """Return a dictionary summarizing the cleaning results."""