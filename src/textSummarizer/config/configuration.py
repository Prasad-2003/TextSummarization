from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import *

class ConfigurationManager:
    
    def __init__(
        self,
        config_path = CONFIG_FILE_PATH,
        params_path = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        
        create_directories([self.config.artifacts_root])
        
        
    def get_dataingestion_config(self) -> dataingestionConfig:
        
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        data_ingestion_config = dataingestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
    
    def get_datavalidation_config(self) -> datavalidationconfig:
        
        config = self.config.data_validation
        
        data_validation_config = datavalidationconfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )
        
        return data_validation_config
    
         
    def get_datatransformation_config(self) -> datatransformationConfig:
        
        config = self.config.data_transformation
        
        create_directories([config.root_dir])
        datatransformation_config = datatransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )
        
        return datatransformation_config
    
    def get_model_trainer_config(self) -> modeltrainerConfig:
        
        config = self.config.model_trainer
        params = self.params.TrainingArguments
        
        create_directories([config.root_dir])
        
        model_trainer_config = modeltrainerConfig(
            root_dir = config.root_dir,
            data_path=config.data_path,
            num_train_epochs=params.num_train_epochs,
            weight_decay = params.weight_decay,
            model_ckpt=config.model_ckpt,
            evaluation_strategy=params.evaluation_strategy,
            logging_steps = params.logging_steps,
            warmup_steps=params.warmup_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            eval_steps=params.eval_steps,
            save_steps=params.save_steps,
            per_device_eval_batch_size=params.per_device_eval_batch_size
        )
        
        return model_trainer_config
    
        
    def get_model_evaluation_config(self) -> modelevaluationconfig:
        
        config = self.config.model_evaluation
        
        model_evaluation_config = modelevaluationconfig(
            root_dir=config.root_dir,
            model_path=config.model_path,
            tokenizer_path=config.tokenizer_path,
            metric_file_name=config.metric_file_name,
            data_path=config.data_path
        )
        
        return model_evaluation_config