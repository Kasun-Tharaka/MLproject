from housing.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelEvaluationConfig, ModelTrainingConfig, ModelEvaluationConfig, ModelPusherConfig, TrainigPippelineConfig
class Configuration:

    def __init__(self) -> None:
        pass

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        pass

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def det_model_trainer_config(self) -> ModelTrainingConfig:
        pass

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass

    def get_trainig_pipeline_config(self) -> TrainigPippelineConfig:
        pass