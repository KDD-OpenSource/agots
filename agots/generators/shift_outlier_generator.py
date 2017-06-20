from .base import OutlierGenerator
from agots.multivariate_generators.multivariate_shift_outlier_generator import MultivariateShiftOutlierGenerator


class ShiftOutlierGenerator(OutlierGenerator):
    def __init__(self, timestamps=[], value=None, shift_value=None):
        OutlierGenerator.__init__(self, timestamps)
        self.value = value
        self.SHIFT_VALUE = shift_value

    def get_value(self, current_timestamp, previous_df):
        generator = MultivariateShiftOutlierGenerator(timestamps=self.timestamps, value=self.value,
                                                      shift_value=self.SHIFT_VALUE)
        return generator.get_value(current_timestamp, previous_df)
