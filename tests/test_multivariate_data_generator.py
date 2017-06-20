import unittest

from agots.multivariate_generators.multivariate_data_generator import MultivariateDataGenerator


class TestMultivariateDataGenerator(unittest.TestCase):
    def get_multivariate_data_generator(self, stream_length=200, n=10, k=5):
        return MultivariateDataGenerator(stream_length, n, k)

    def test_generate_baseline(self):
        STREAM_LENGTH = 200
        N = 10
        K = 5
        dg = MultivariateDataGenerator(STREAM_LENGTH, N, K)
        df = dg.generate_baseline()
        df_cor = df.corr()

        self.assertEqual(len(df), STREAM_LENGTH)
        self.assertEqual(len(df.columns), N)

        # The first K columns should heavily correlate
        for i in range(K):
            self.assertGreaterEqual(df_cor.iloc[0, i], 0.9)

        # The remaining N-K columns should not correlate
        for i in range(K, N):
            self.assertLessEqual(df_cor.iloc[0, i], 0.7)

    def test_generation_different_number_dimension(self):
        n = 5
        dg = self.get_multivariate_data_generator(n=n, k=4)
        df = dg.generate_baseline()
        (_, dimensions) = df.shape
        self.assertTrue(dimensions, n)

    def test_generation_same_number_dimension(self):
        n = 5
        dg = self.get_multivariate_data_generator(n=n, k=n-1)
        df = dg.generate_baseline()
        (_, dimensions) = df.shape
        self.assertTrue(dimensions, n)

    def test_defined_initial_value(self):
        initial_value = 2
        dg = self.get_multivariate_data_generator()
        df = dg.generate_baseline(initial_value_min=initial_value, initial_value_max=initial_value)
        self.assertEqual(df.iloc[0, 0], initial_value)

    def test_random_initial_value(self):
        initial_value_min = 2
        initial_value_max = 5
        n = 10
        dg = self.get_multivariate_data_generator(n=n)
        df = dg.generate_baseline(initial_value_min=initial_value_min, initial_value_max=initial_value_max)
        for i in range(n):
            self.assertGreaterEqual(df.iloc[0, i], initial_value_min)
            self.assertLessEqual(df.iloc[0, i], initial_value_max)

    def test_random_negative_initial_value(self):
        initial_value_min = -10
        initial_value_max = 10
        n = 10
        dg = self.get_multivariate_data_generator(n=n)
        df = dg.generate_baseline(initial_value_min=initial_value_min, initial_value_max=initial_value_max)
        for i in range(n):
            self.assertGreaterEqual(df.iloc[i, 0], initial_value_min)
            self.assertLessEqual(df.iloc[i, 0], initial_value_max)

    def test_random_both_negative_initial_value(self):
        initial_value_min = -10
        initial_value_max = -2
        n = 10
        dg = self.get_multivariate_data_generator(n=n)
        df = dg.generate_baseline(initial_value_min=initial_value_min, initial_value_max=initial_value_max)
        for i in range(n):
            self.assertGreaterEqual(df.iloc[i, 0], initial_value_min)
            self.assertLessEqual(df.iloc[i, 0], initial_value_max)

    def test_add_outliers_extreme(self):
        dg = self.get_multivariate_data_generator()
        _ = dg.generate_baseline()
        df = dg.add_outliers({'extreme': [{'n': 0, 'timestamps': [(3,)]}]})
        self.assertGreater(abs(df.iloc[3, 0]), abs(4 * df.iloc[:3, 0].mean()))

    def test_create_correlating_time_series(self):
        n = 5
        dg = self.get_multivariate_data_generator(n=n, k=n-1)
        df = dg.init_dataframe(n)
        df = dg.create_basic_time_series(df)
        df = dg.create_correlating_time_series(number_time_series=n, correlation_min=0.7, df=df)

        (_, dimensions) = df.shape
        self.assertTrue(dimensions, n)
