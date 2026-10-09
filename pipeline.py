##day1
# Starter Code
## `pipeline.py`

"""
Data Processing Pipeline - CLI Template
DS 3500 - MP1
Usage:
python pipeline.py --input data.csv --output clean.csv
python pipeline.py --input data.csv --output results.json --format json --
verbose
"""
import argparse
from html import parser
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",datefmt="%H:%M:%S"
    )
    return logging.getLogger(__name__)

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Data Processing Pipeline")
    
    parser.add_argument(
    "--input", "-i", 
    required=True, 
    help="Path to the input data file")
    
    parser.add_argument(
    "--output", "-o", 
    required=True, 
    help="Path to the output data file"
)   
    parser.add_argument(
    "--format",
    choices=["csv", "json"],
    default="csv",
    help="Output format"
)   
    parser.add_argument(
    "--verbose", "-v",
    action="store_true",
    help="Enable verbose logging"
)
    return parser.parse_args()

 # TODO: implement
def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    if not Path(filepath).is_file(): 
        logger.error(f"Input File Not Found: {filepath}")
        return False
    else: 
        logger.info(f"Input File Vaidated: {filepath}")
        return True 
   


def main():
    """Main pipeline function"""
    args = parse_arguments()
    setup_logging(args.verbose)
    logger.debug(
        f"Arguments parsed: input={args.input}, output={args.output}, format={args.format}") 
    if not validate_input(args.input): 
        sys.exit(1) 

        
 # TODO: implement
if __name__ == "__main__":
    main()
