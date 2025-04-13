from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logger

STAGE_NAME = "DATA_INGESTION_STAGE"
try:
    logger.info(f"STAGE -- {STAGE_NAME} INITIATED")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"STAGE -- {STAGE_NAME} COMPLETED")
    
except Exception as e:
    logger.exception(e)
    raise e 