from .base import OutlierGenerator
from agots.multivariate_generators.multivariate_variance_outlier_generator import MultivariateVarianceOutlierGenerator


class VarianceOutlierGenerator(OutlierGenerator):
    def __init__(self, timestamps=[], variance_factor=3):
        OutlierGenerator.__init__(self, timestamps)
        self.VARIANCE_FACTOR = variance_factor

    def get_value(self, current_timestamp, previous_df):
        generator = MultivariateVarianceOutlierGenerator(timestamps=self.timestamps,
                                                         variance_factor=self.VARIANCE_FACTOR)
        return generator.get_value(current_timestamp, previous_df)
