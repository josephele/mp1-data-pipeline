# src/data_validator.py
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def validate_dataframe(df, required_columns, numeric_columns):
    """Validate the DataFrame and return valid data.
    required_columns: a list of column names that must exist.
    numeric_columns: a list of column names whose values should be
    numeric.
    """
    before = len(df)
    for col in required_columns:
        if col not in df.columns:
            logger.error(f"Column missing:{col}")
            raise ValueError(f"column missing: {col}")
    for col in numeric_columns:
            invalid_rows = []
            for i, value in df[col].items():
                if pd.notna(value):
                    try:
                        float(value)
                    except ValueError:
        # TODO: Log a warning and record this row's index.
                        logger.warning(f"Remove rows, not numeric{col}")
                        invalid_rows = invalid_rows + [i]
        # TODO: Remove the invalid rows.
        #convert to a numeric data type
            df = df.drop(invalid_rows)
            df[col] = pd.to_numeric(df[col])
    logger.debug(f"Valid rows: {len(df)}, removed:{before - len(df)}")
    return df
