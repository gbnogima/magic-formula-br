from abc import ABC, abstractmethod
import pandas as pd

class DataSource(ABC):

    def __init__(self, reuse_file):
        self.reuse_file = reuse_file

    @abstractmethod
    def get_strategy(self) -> str:
        pass

    @abstractmethod
    def build_dataframe(self, reuse_file) -> pd.DataFrame:
        pass
