from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationTraningPipeline
from src.textSummarizer.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.textSummarizer.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline
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


STAGE_NAME = "DATA_TRANSFORMATION_STAGE"
try:
    logger.info(f"STAGE -- {STAGE_NAME} INITIATED")
    data_transformation_pipeline = DataTransformationTraningPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"STAGE -- {STAGE_NAME} COMPLETED")
    
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "MODEL_TRAINER_PIPELINE"
try:
    logger.info(f"STAGE -- {STAGE_NAME} INITIATED")
    model_trainer_pipeline = ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f"STAGE -- {STAGE_NAME} COMPLETED")
    
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
