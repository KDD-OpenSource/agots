class OutlierGenerator:
    def __init__(self, timestamps=[]):
        self.timestamps = timestamps

    def get_value(self, current_timestamp, previous_df):
        return NotImplementedError
