import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.data_loader import DataLoader
from app.mlflow_manager import MLflowManager
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

def run_experiment(data_version: str = None):
    """运行完整的 ML 实验流程"""
    
    # 初始化管理器
    data_loader = DataLoader()
    mlflow_manager = MLflowManager(experiment_name="iris-classification")
    
    # 开始 MLflow 运行
    with mlflow_manager.start_experiment(run_name=f"experiment_{data_version or 'latest'}"):
        
        # 1. 加载数据（使用 DVC 版本控制）
        print("加载数据...")
        df = data_loader.load_dataset("raw/iris.csv", version=data_version)
        
        # 记录数据版本信息
        mlflow_manager.log_dataset_version("raw/iris.csv", data_version or "latest")
        
        # 2. 准备数据
        X = df.drop('species', axis=1)
        y = df['species']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # 3. 定义和训练模型
        params = {
            "n_estimators": 100,
            "max_depth": 5,
            "random_state": 42
        }
        
        print("训练模型...")
        model = RandomForestClassifier(**params)
        model.fit(X_train, y_train)
        
        # 4. 记录参数和指标
        mlflow_manager.log_parameters(params)
        
        # 计算指标
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        metrics = {
            "accuracy": accuracy,
            "train_samples": len(X_train),
            "test_samples": len(X_test)
        }
        
        mlflow_manager.log_metrics(metrics)
        
        # 5. 记录模型
        mlflow_manager.log_model(model, "random_forest_model")
        
        print(f"实验完成！准确率: {accuracy:.4f}")
        
        return model, accuracy

if __name__ == "__main__":
    # 运行实验（可以指定数据版本）
    model, accuracy = run_experiment()