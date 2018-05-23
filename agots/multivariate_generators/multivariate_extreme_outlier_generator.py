import numpy as np

from .base import MultivariateOutlierGenerator


class MultivariateExtremeOutlierGenerator(MultivariateOutlierGenerator):
    def __init__(self, timestamps=None, value=None):
        self.timestamps = [] if timestamps is None else list(sum(timestamps, ()))
        self.value = value
        self.VALUE_FACTOR = 5

    def get_value(self, current_timestamp, previous_df):
        if current_timestamp in self.timestamps:
            if self.value is None:
                previous_mean = previous_df.mean()
                return np.random.random() + previous_mean * self.VALUE_FACTOR
            else:
                return self.value
        else:
            return 0

    def add_outliers(self, df):
        additional_values = []
        for timestamp_index in range(len(df)):
            additional_values.append(self.get_value(timestamp_index, df.iloc[:timestamp_index]))
        return additional_values
