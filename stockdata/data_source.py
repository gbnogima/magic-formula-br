from abc import ABC, abstractmethod
import pandas as pd

class DataSource(ABC):

    @abstractmethod
    def get_strategy(self) -> str:
        pass

    @abstractmethod
    def build_dataframe(self) -> pd.DataFrame:
        pass
