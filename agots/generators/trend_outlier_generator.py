from .base import OutlierGenerator
from agots.multivariate_generators.multivariate_trend_outlier_generator import MultivariateTrendOutlierGenerator


class TrendOutlierGenerator(OutlierGenerator):
    def __init__(self, timestamps=[], trend_value=0.06):
        OutlierGenerator.__init__(self, timestamps)
        self.TREND_VALUE = trend_value

    def get_value(self, current_timestamp, previous_df):
        generator = MultivariateTrendOutlierGenerator(timestamps=self.timestamps, trend_value=self.TREND_VALUE)
        return generator.get_value(current_timestamp, previous_df)
