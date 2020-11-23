import numpy as np
import pandas as pd

from datetime import time
from datetime import datetime
from datetime import timezone

from pandas.core.groupby import DataFrameGroupBy
from pandas.core.window import RollingGroupby

class StockFrame():
    def __init__(self, data: list[dict]):
        self._data = data
        self._frame = self.create_frame()
        self._symbol_groups = None
        self._symbol_rolling_groups = None

    @property
    def frame(self):
        return self._frame

    @property
    def symbol_groups(self):

        self._symbol_groups = self._frame.groupby(
            by= 'symbol',
            as_index=False,
            sort = True
        )

        return self._symbol_groups

    def symbol_rolling_groups(self, size):
        if not self._symbol_groups:
            self.symbol_groups

        self._symbol_rolling_groups = self._symbol_groups.rolling(size)

        return self._symbol_rolling_groups

    def create_frame(self):
        price_df = pd.DataFrame(data=self._data)
        price_df = self.parse_datetime_column(price_df)
        price_df = self.set_multi_index(price_df)

        return price_df

    def parse_datetime_column(self, price_df):
        price_df['datetime'] = pd.to_datetime(price_df['datetime'], unit= 'ms', origin= 'unix')
        return price_df

    def set_multi_index(self, price_df):
        price_df = price_df.set_index(key=['symbol', 'datetime'])
        return price_df

    def add_rows(self):
        pass