import numpy as np

from .base import MultivariateOutlierGenerator


class MultivariateVarianceOutlierGenerator(MultivariateOutlierGenerator):
    def __init__(self, timestamps=None, factor=8):
        self.timestamps = timestamps or []
        self.factor = factor

    def add_outliers(self, timeseries):
        additional_values = np.zeros(timeseries.size)
        for start, end in self.timestamps:
            difference = np.diff(timeseries[start-1:end]) if start > 0 \
                         else np.insert(np.diff(timeseries[start:end]), 0, 0)
            additional_values[list(range(start, end))] += (self.factor - 1) * difference
        return additional_values
