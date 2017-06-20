class MultivariateOutlierGenerator:
    def __init__(self, timestamps):
        self.timestamps = timestamps

    def get_values(self, current_timestamp, previous_df):
        return NotImplementedError

    def add_outliers(self, df):
        return NotImplementedError
