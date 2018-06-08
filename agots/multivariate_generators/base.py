class MultivariateOutlierGenerator:
    def __init__(self, timestamps):
        self.timestamps = timestamps

    def get_value(self, current_timestamp, timeseries):
        return NotImplementedError

    def add_outliers(self, timeseries):
        return NotImplementedError
