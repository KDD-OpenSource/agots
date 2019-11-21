# agots
Anomaly Generator on Time Series

## Requirements
- Python 3
- Install the dependencies via
`pip install -r requirements.txt`

## Usage
The following example generates 4 time series with 200 data points. The first two time series correlate:  

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from agots.multivariate_generators.multivariate_data_generator import MultivariateDataGenerator

STREAM_LENGTH = 200
N = 4
K = 2

dg = MultivariateDataGenerator(STREAM_LENGTH, N, K)
df = dg.generate_baseline(initial_value_min=-4, initial_value_max=4)

for col in df.columns:
    plt.plot(df[col], label=col)
plt.legend()
plt.show()

df.corr()
```
![first](https://user-images.githubusercontent.com/6676439/69345843-1e288b00-0c72-11ea-8d3c-cf67c88d42d6.png)  

To add anomalies, just specify their types and the locations within the corresponding time series as well as their magnitudes:  

```python
df = dg.add_outliers({'extreme': [{'n': 0, 'timestamps': [(10,), (30,)],
                                   'factor': 10
                                   }],
                      'shift':   [{'n': 1, 'timestamps': [(40, 60)],
                                   'factor': 10
                                   }],
                      'trend':   [{'n': 2, 'timestamps': [(70, 90)],
                                   'factor': 5
                                   }],
                      'variance': [{'n': 3, 'timestamps': [(100, 150)],
                                    'factor': 10
                                    }]})

for col in df.columns:
    plt.plot(df[col], label=col)
plt.legend()
plt.show()

```
![second](https://user-images.githubusercontent.com/6676439/69345894-297bb680-0c72-11ea-94e0-d0ea3ae32c7a.png)

Discover more in [`examples/`](https://github.com/KDD-OpenSource/agots/tree/master/examples).
