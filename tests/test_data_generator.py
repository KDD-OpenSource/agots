import unittest
import pandas as pd

from agots.generators.extreme_outlier_generator import ExtremeOutlierGenerator
from agots.generators.data_generator import DataGenerator


class TestDataGenerator(unittest.TestCase):
    def test_number_generated_dimensions(self):
        stream_length = 200
        extreme_gens = [ExtremeOutlierGenerator(timestamps=[(140,)], value=5)]

        dg = DataGenerator(stream_length, extreme_gens)
        df = dg.run()
        (_, width) = df.shape
        # one dimension is the timestamp, is also set as index
        self.assertTrue(width, 2)

    def test_type_get_value(self):
        stream_length = 200
        extreme_gens = [ExtremeOutlierGenerator(timestamps=[(140,)], value=5)]

        dg = DataGenerator(stream_length, extreme_gens)
        df = dg.run()
        self.assertEqual(type(df), type(pd.DataFrame()))
