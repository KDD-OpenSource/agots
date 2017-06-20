from .base import OutlierGenerator
from agots.multivariate_generators.multivariate_extreme_outlier_generator import MultivariateExtremeOutlierGenerator


class ExtremeOutlierGenerator(OutlierGenerator):
    def __init__(self, timestamps=[], value=None):
        OutlierGenerator.__init__(self, timestamps)
        self.value = value
        self.PREVIOUS_MEAN = None
        self.VALUE_FACTOR = 5

    def get_value(self, current_timestamp, previous_df):
        generator = MultivariateExtremeOutlierGenerator(timestamps=self.timestamps, value=self.VALUE_FACTOR)
        return generator.get_value(current_timestamp, previous_df)
