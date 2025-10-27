
from typing import Any, Dict, Optional

import mlflow
import mlflow.sklearn


class MLflowManager:
    def __init__(self, tracking_uri: str = "mlruns", experiment_name: str = "default"):
        """
        MLflow 管理器

        Args:
            tracking_uri: MLflow 跟踪 URI
            experiment_name: 实验名称
        """
        mlflow.set_tracking_uri(tracking_uri)
        mlflow.set_experiment(experiment_name)
        self.experiment_name = experiment_name

    def start_experiment(
        self, run_name: Optional[str] = None, tags: Optional[Dict[str, Any]] = None
    ) -> mlflow.ActiveRun:
        """开始新的实验运行"""
        return mlflow.start_run(run_name=run_name, tags=tags)

    def log_parameters(self, params: Dict[str, Any]):
        """记录参数"""
        mlflow.log_params(params)

    def log_metrics(self, metrics: Dict[str, float], step: Optional[int] = None):
        """记录指标"""
        mlflow.log_metrics(metrics, step=step)

    def log_dataset_version(self, data_path: str, data_version: str):
        """记录数据集版本信息"""
        mlflow.log_param("data_path", data_path)
        mlflow.log_param("data_version", data_version)

    def log_model(
        self,
        model,
        model_name: str,
        signature=None,
        input_example=None,
        registered_model_name: Optional[str] = None,
    ):
        """记录模型"""
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path=model_name,
            signature=signature,
            input_example=input_example,
            registered_model_name=registered_model_name,
        )

    def end_run(self):
        """结束当前运行"""
        mlflow.end_run()
