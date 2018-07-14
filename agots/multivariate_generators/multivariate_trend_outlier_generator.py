import numpy as np

from .base import MultivariateOutlierGenerator


class MultivariateTrendOutlierGenerator(MultivariateOutlierGenerator):
    def __init__(self, timestamps=None, factor=8):
        self.timestamps = timestamps or []
        self.factor = factor / 40  # Adjust for trend

    def add_outliers(self, timeseries):
        additional_values = np.zeros(timeseries.size)
        for start, end in self.timestamps:
            slope = np.random.choice([-1, 1]) * self.factor * np.arange(end - start)
            additional_values[list(range(start, end))] += slope
            additional_values[end:] += slope[-1]
        return additional_values
