import numpy as np

from .base import MultivariateOutlierGenerator


class MultivariateExtremeOutlierGenerator(MultivariateOutlierGenerator):
    def __init__(self, timestamps=None, factor=1):
        self.timestamps = [] if timestamps is None else list(sum(timestamps, ()))
        self.factor = factor

    def get_value(self, current_timestamp, timeseries):
        if current_timestamp in self.timestamps:
            local_std = timeseries.iloc[max(0, current_timestamp - 10):current_timestamp + 10].std()
            return np.random.choice([-1, 1]) * self.factor * local_std
        else:
            return 0

    def add_outliers(self, timeseries):
        additional_values = []
        for timestamp_index in range(len(timeseries)):
            additional_values.append(self.get_value(timestamp_index, timeseries))
        return additional_values
