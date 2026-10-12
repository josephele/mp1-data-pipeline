# Write a short paragraph of 5-8 sentences describing what your pipeline does, how data movesthrough it, how your completed pipeline is organized, and the main responsibility of each module.

# Include an example command to run the pipeline with the provided sample data and the output produced by your code.

This pipeline is able to take data that is inconsistant and clean it through validating data and catching errors. Once a csv or other file is inputed, you are able to direct the main pipeline on what rules to follow when cleaning the data with config.yaml. Then the data moves through the pipeline and the pipeline redirects the data to the files in src folder. Within this folder we have multiple modules with different purposes; utils.py sets up logging for the pipeline, data_loaders.py loads data based on the files extension, and data_validator makes sure that columns and numeric columns match up with the data. Data processor helps clean the data and get rid of empty rows/columns. After data processor, the data can be saved with the data output file. 

# example commnand to run the entire pipeline:
 python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose

# output:
 19:34:07 DEBUG    __main__ — Arguments parsed: input=fixtures/sample_data.csv, config=config/config.yaml, output=output/clean.csv
19:34:07 INFO     src.utils — Input file validated: fixtures/sample_data.csv
19:34:07 INFO     src.utils — Input file validated: config/config.yaml
19:34:07 INFO     src.data_loaders — Loaded CSV file: fixtures/sample_data.csv(100)rows
19:34:07 INFO     root — Loaded YAML file: config/config.yaml
19:34:07 WARNING  src.data_validator — Remove rows, not numericrating
19:34:07 WARNING  src.data_validator — Remove rows, not numericrating
19:34:07 DEBUG    src.data_validator — Valid rows: 98, removed:2
19:34:07 INFO     __main__ — Validated: 100 to 98
19:34:07 DEBUG    src.data_processor — remove_duplicates: 98 to 96 rows
19:34:07 DEBUG    src.data_processor — handle_missing: 96 to 94 rows
19:34:07 DEBUG    src.data_processor — rating: method=iqr, threshold 1.5, removed = 2
19:34:07 INFO     __main__ — Processing results98 to 92 rows
19:34:07 DEBUG    src.data_output — Saved 92 rows output/clean.csv
19:34:07 INFO     __main__ — Save clean dataoutput/clean.csv
{'rows_before': 98, 'rows_after': 92, 'rows_removed': 6, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}
(venv) (base) elesajoseph@Elesas-MacBook-Pro mp1-data-pipeline % 