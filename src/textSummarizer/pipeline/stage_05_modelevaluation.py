from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import *
from textSummarizer.logging import logger


class modeltrainerpipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        modelevaluation_config = config.get_model_evaluation_config()
        modelevaluation = modelevaluation(config=modelevaluation_config)
        modelevaluation.evaluate()
