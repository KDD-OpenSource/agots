import numpy as np

from .base import MultivariateOutlierGenerator


class MultivariateVarianceOutlierGenerator(MultivariateOutlierGenerator):
    def __init__(self, timestamps=None, variance_factor=3):
        self.timestamps = timestamps or []
        self.VARIANCE_FACTOR = variance_factor
        self.ongoing_variance = False

        np.random.seed(1337)

    def get_value(self, current_timestamp, previous_df):
        start_timestamps = [start for start, _ in self.timestamps]
        end_timestamps = [end for _, end in self.timestamps]

        if current_timestamp in end_timestamps:
            self.ongoing_variance = False

        if current_timestamp in start_timestamps or self.ongoing_variance:
            self.ongoing_variance = True
            return np.random.random() * self.VARIANCE_FACTOR
        else:
            return 0

    def add_outliers(self, df):
        additional_values = []
        for timestamp_index in range(len(df)):
            additional_values.append(self.get_value(timestamp_index, None))
        return additional_values
