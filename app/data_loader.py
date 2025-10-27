import pandas as pd
import dvc.api
import os
from typing import Optional


class DataLoader:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir

    def load_dataset(
        self, file_path: str, version: Optional[str] = None
    ) -> pd.DataFrame:
        """
        使用 DVC 加载指定版本的数据集

        Args:
            file_path: 数据文件路径（相对于 data_dir）
            version: Git commit hash 或 tag，None 表示最新版本

        Returns:
            pandas DataFrame
        """
        full_path = os.path.join(self.data_dir, file_path)

        try:
            with dvc.api.open(path=full_path, rev=version, mode="r") as fd:
                df = pd.read_csv(fd)
                print(f"成功加载数据: {file_path}, 版本: {version or 'latest'}")
                return df
        except Exception as e:
            print(f"加载数据失败: {e}")
            raise

    def get_data_versions(self, file_path: str):
        """获取数据文件的所有版本"""
        # 这里可以扩展为通过 Git 历史获取版本信息
        print("使用 'git log --oneline' 查看数据文件版本历史")
