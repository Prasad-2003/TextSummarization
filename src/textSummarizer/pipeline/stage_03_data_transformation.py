from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import *
from textSummarizer.logging import logger

class datatransformationpipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_datatransformation_config()
        datavalidation = data_transformation(config=data_transformation_config)
        datavalidation.create_dataset()