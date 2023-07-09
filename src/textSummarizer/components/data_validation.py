import os
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import *

class DataValidation:
    
    def __init__(self, config:datavalidationconfig):
        self.config = config
        
    def validate_all_files(self) -> bool:
        try:
            
            validation_status = True
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            with open(self.config.STATUS_FILE, 'w') as fp: 
                for file in self.config.ALL_REQUIRED_FILES:
                    if file not in all_files:
                        logger.info(f"{file} not found!")
                        validation_status = False
                        fp.write(f'{file} data file validation status: {validation_status}\n')
                    else:
                        validation_status = True
                        fp.write(f'{file} data file validation status: {validation_status}\n')
                fp.close()
            return validation_status
        
        except Exception as e:
            raise e