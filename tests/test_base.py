import unittest
import pandas as pd

from agots.generators.extreme_outlier_generator import ExtremeOutlierGenerator
from agots.generators.shift_outlier_generator import ShiftOutlierGenerator
from agots.generators.trend_outlier_generator import TrendOutlierGenerator
from agots.generators.variance_outlier_generator import VarianceOutlierGenerator


class TestBase(unittest.TestCase):
    # ExtremeValueGenerator
    def test_get_value_extreme_empty_df(self):
        df = pd.DataFrame(columns=['timestamp', 'value'])
        df.set_index('timestamp', inplace=True)
        generator = ExtremeOutlierGenerator(timestamps=[(20,)], value=5)
        self.assertEqual(type(generator.get_value(current_timestamp=0, previous_df=df)), int)

    def test_get_value_extreme_at_outlier(self):
        df = pd.DataFrame(columns=['timestamp', 'value'])
        df.set_index('timestamp', inplace=True)
        df = pd.concat([pd.DataFrame([5], columns=['value']) for i in range(200)], ignore_index=True)
        generator = ExtremeOutlierGenerator(timestamps=[(20,)], value=5)
        self.assertEqual(type(generator.get_value(current_timestamp=20, previous_df=df)), int)

    def test_get_value_extreme_not_at_outlier(self):
        df = pd.DataFrame(columns=['timestamp', 'value'])
        df.set_index('timestamp', inplace=True)
        df = pd.concat([pd.DataFrame([5], columns=['value']) for i in range(200)], ignore_index=True)
        generator = ExtremeOutlierGenerator(timestamps=[(20,)], value=5)
        self.assertEqual(type(generator.get_value(current_timestamp=15, previous_df=df)), int)

    # ShiftOutlierGenerator
    def test_get_value_shift_empty_df(self):
        df = pd.DataFrame(columns=['timestamp', 'value'])
        df.set_index('timestamp', inplace=True)
        generator = ShiftOutlierGenerator(timestamps=[(20, 25)], value=5)
        self.assertEqual(type(generator.get_value(current_timestamp=0, previous_df=df)), int)

    def test_get_value_shift_at_outlier(self):
        df = pd.DataFrame(columns=['timestamp', 'value'])
        df.set_index('timestamp', inplace=True)
        df = pd.concat([pd.DataFrame([5], columns=['value']) for i in range(200)], ignore_index=True)
        generator = ShiftOutlierGenerator(timestamps=[(20, 25)], value=7)
        self.assertEqual(type(generator.get_value(current_timestamp=21, previous_df=df)), int)

    def test_get_value_shift_not_at_outlier(self):
        df = pd.DataFrame(columns=['timestamp', 'value'])
        df.set_index('timestamp', inplace=True)
        df = pd.concat([pd.DataFrame([5], columns=['value']) for i in range(200)], ignore_index=True)
        generator = ShiftOutlierGenerator(timestamps=[(20, 25)], value=5)
        self.assertEqual(type(generator.get_value(current_timestamp=15, previous_df=df)), int)

    # TrendOutlierGenerator
    def test_get_value_trend_empty_df(self):
        df = pd.DataFrame(columns=['timestamp', 'value'])
        df.set_index('timestamp', inplace=True)
        generator = TrendOutlierGenerator(timestamps=[(20, 25)])
        self.assertEqual(type(generator.get_value(current_timestamp=0, previous_df=df)), int)

    def test_get_value_trend_at_outlier(self):
        df = pd.DataFrame(columns=['timestamp', 'value'])
        df.set_index('timestamp', inplace=True)
        df = pd.concat([pd.DataFrame([5], columns=['value']) for i in range(200)], ignore_index=True)
        generator = TrendOutlierGenerator(timestamps=[(20, 25)])
        self.assertEqual(type(generator.get_value(current_timestamp=22, previous_df=df)), int)

    def test_get_value_trend_not_at_outlier(self):
        df = pd.DataFrame(columns=['timestamp', 'value'])
        df.set_index('timestamp', inplace=True)
        df = pd.concat([pd.DataFrame([5], columns=['value']) for i in range(200)], ignore_index=True)
        generator = TrendOutlierGenerator(timestamps=[(20, 25)])
        self.assertEqual(type(generator.get_value(current_timestamp=15, previous_df=df)), int)

    # VarianceOutlierGenerator
    def test_get_value_variance_empty_df(self):
        df = pd.DataFrame(columns=['timestamp', 'value'])
        df.set_index('timestamp', inplace=True)
        generator = VarianceOutlierGenerator(timestamps=[(20, 25)])
        self.assertEqual(type(generator.get_value(current_timestamp=0, previous_df=df)), int)

    def test_get_value_variance_at_outlier(self):
        df = pd.DataFrame(columns=['timestamp', 'value'])
        df.set_index('timestamp', inplace=True)
        df = pd.concat([pd.DataFrame([5], columns=['value']) for i in range(200)], ignore_index=True)
        generator = VarianceOutlierGenerator(timestamps=[(20, 25)])
        self.assertEqual(type(generator.get_value(current_timestamp=23, previous_df=df)), int)

    def test_get_value_variance_not_at_outlier(self):
        df = pd.DataFrame(columns=['timestamp', 'value'])
        df.set_index('timestamp', inplace=True)
        df = pd.concat([pd.DataFrame([5], columns=['value']) for i in range(200)], ignore_index=True)
        generator = VarianceOutlierGenerator(timestamps=[(20, 25)])
        self.assertEqual(type(generator.get_value(current_timestamp=15, previous_df=df)), int)
