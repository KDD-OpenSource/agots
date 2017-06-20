import numpy as np

from .base import MultivariateOutlierGenerator


class MultivariateTrendOutlierGenerator(MultivariateOutlierGenerator):
    def __init__(self, timestamps=None, trend_value=0.06):
        self.timestamps = timestamps or []
        self.TREND_VALUE = trend_value
        self.trend_since = 0
        self.ongoing_trend = False

        np.random.seed(1337)

    def get_value(self, current_timestamp, previous_df):
        start_timestamps = [start for start, _ in self.timestamps]
        end_timestamps = [end for _, end in self.timestamps]

        if current_timestamp in end_timestamps:
            self.ongoing_trend = False
            self.trend_since = 0

        if current_timestamp in start_timestamps or self.ongoing_trend:
            self.ongoing_trend = True
            self.trend_since += 1
            return np.random.random() + self.TREND_VALUE * self.trend_since
        else:
            return 0

    def add_outliers(self, df):
        additional_values = []
        for timestamp_index in range(len(df)):
            additional_values.append(self.get_value(timestamp_index, None))
        return additional_values
