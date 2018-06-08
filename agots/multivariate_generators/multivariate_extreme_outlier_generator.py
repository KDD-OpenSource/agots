import numpy as np

from .base import MultivariateOutlierGenerator


class MultivariateExtremeOutlierGenerator(MultivariateOutlierGenerator):
    def __init__(self, timestamps=None, value=None):
        self.timestamps = [] if timestamps is None else list(sum(timestamps, ()))
        self.value = value
        self.VALUE_FACTOR = 5

    def get_value(self, current_timestamp, timeseries):
        if current_timestamp in self.timestamps:
            if self.value is None:
                local_mean = timeseries.iloc[max(0, current_timestamp - 10):current_timestamp + 10].mean()
                return np.random.random() + local_mean * self.VALUE_FACTOR
            else:
                return self.value
        else:
            return 0

    def add_outliers(self, timeseries):
        additional_values = []
        for timestamp_index in range(len(timeseries)):
            additional_values.append(self.get_value(timestamp_index, timeseries))
        return additional_values
