import numpy as np

from .base import MultivariateOutlierGenerator


class MultivariateShiftOutlierGenerator(MultivariateOutlierGenerator):
    def __init__(self, timestamps=None, value=None, shift_value=None):
        timestamps = timestamps or []
        self.timestamps = timestamps
        self.value = value
        self.SHIFT_VALUE = shift_value
        self.MEAN_FACTOR = 5
        self.ongoing_shift = False

        np.random.seed(1337)

    def get_value(self, current_timestamp, previous_df_series):
        start_timestamps = [start for start, _ in self.timestamps]
        end_timestamps = [end for _, end in self.timestamps]

        if current_timestamp in end_timestamps:
            self.ongoing_shift = False

        if current_timestamp in start_timestamps or self.ongoing_shift:
            self.ongoing_shift = True
            if self.value is None:
                if self.SHIFT_VALUE is None:
                    self.SHIFT_VALUE = previous_df_series.mean() * self.MEAN_FACTOR
                return np.random.random() + self.SHIFT_VALUE
            else:
                return self.value
        else:
            return 0

    def add_outliers(self, df):
        additional_values = []
        for timestamp_index in range(len(df)):
            additional_values.append(self.get_value(timestamp_index, df.iloc[:timestamp_index]))
        return additional_values
