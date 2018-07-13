class MultivariateOutlierGenerator:
    def __init__(self, timestamps):
        self.timestamps = timestamps

    def add_outliers(self, timeseries):
        return NotImplementedError
