from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import *
from textSummarizer.logging import logger

class modeltrainerpipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        modelTrainer = modelTrainer(config=model_trainer_config)
        modelTrainer.train()