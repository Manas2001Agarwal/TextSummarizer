from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.logging import logger
from src.textSummarizer.components.data_transformation import DataTransformation

class DataTransformationTraningPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        config_manager = ConfigurationManager()
        data_transformation_config = config_manager.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.convert()