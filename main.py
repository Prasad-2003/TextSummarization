from textSummarizer.pipeline.stage_01_dataingestion import dataingestionpipeline
from textSummarizer.logging import logger

stage_name = "data ingestion stage."

try:
    logger.info("f>>>>> {stage_name} started <<<<<<")
    data_ingestion = dataingestionpipeline()
    data_ingestion.main()
    logger.info("f>>>>> {stage_name} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e