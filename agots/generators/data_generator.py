import pandas as pd
import numpy as np

COLUMNS = ['timestamp', 'value']


class DataGenerator:
    def __init__(self, stream_length, generators=[]):
        self.stream_length = stream_length
        self.generators = generators

    def run(self):
        df = pd.DataFrame(columns=COLUMNS)
        df.set_index('timestamp', inplace=True)

        if self.generators:
            for i in range(self.stream_length):
                value = 0

                for generator in self.generators:
                    value += generator.get_value(i, df)

                if value == 0:
                    value = np.random.random()

                series = dict(zip(COLUMNS, [i, value]))
                df = df.append(series, ignore_index=True)
            return df
        else:
            for i in range(self.stream_length):
                value = 0
                series = dict(zip(COLUMNS, [i, value]))
                df = df.append(series, ignore_index=True)
