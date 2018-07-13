import numpy as np

from .base import MultivariateOutlierGenerator


class MultivariateShiftOutlierGenerator(MultivariateOutlierGenerator):
    def __init__(self, timestamps=None, factor=5):
        timestamps = timestamps or []
        self.timestamps = timestamps
        self.factor = factor

    def add_outliers(self, timeseries):
        additional_values = np.zeros(timeseries.size)
        for start, end in self.timestamps:
            local_std = timeseries.iloc[max(0, start - 10):end + 10].std()
            additional_values[list(range(start, end, 1))] = np.random.choice([-1, 1]) * self.factor * local_std
        return additional_values
