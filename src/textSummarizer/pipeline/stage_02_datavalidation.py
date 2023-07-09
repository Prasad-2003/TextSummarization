from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import *
from textSummarizer.logging import logger

class datavalidationpipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_datavalidation_config()
        datavalidation = DataValidation(config=data_validation_config)
        datavalidation.validate_all_files()