from textSummarizer.pipeline.stage_01_dataingestion import dataingestionpipeline
from textSummarizer.pipeline.stage_02_datavalidation import datavalidationpipeline
from textSummarizer.pipeline.stage_03_data_transformation import datatransformationpipeline
from textSummarizer.pipeline.stage_04_modeltrainer import modeltrainerpipeline
from textSummarizer.pipeline.stage_05_modelevaluation import modelevaluationpipeline
from textSummarizer.logging import logger

stage_name = "data ingestion stage."

try:
    logger.info(f">>>>> {stage_name} started <<<<<<")
    data_ingestion = dataingestionpipeline()
    data_ingestion.main()
    logger.info(f">>>>> {stage_name} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = "data validation stage"

try:
    logger.info(f">>>>> {stage_name} started <<<<<<")
    data_validation = datavalidationpipeline()
    data_validation.main()
    logger.info(f">>>>> {stage_name} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = "data transformation"

try:
    logger.info(f">>>>> {stage_name} started <<<<<<")
    data_transformation = datatransformationpipeline()
    data_transformation.main()
    logger.info(f">>>>> {stage_name} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = "model evaluation"

try:
    logger.info(f">>>> {stage_name} started <<<<<")
    model_evaluation = modelevaluationpipeline()
    model_evaluation.main()
    logger.info(f">>>>> {stage_name} completed <<<<<")
    
except Exception as ee:
    logger.exception(e)
    raise e

