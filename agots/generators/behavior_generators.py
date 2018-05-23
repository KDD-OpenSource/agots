import numpy as np


def sine_generator(cycle_duration=np.random.randint(5, 50),
                   phase_shift=np.random.uniform(0, 2*np.pi),
                   amplitude=np.random.uniform(0, 3)):
    phase_angle = 2*np.pi / cycle_duration
    while True:
        value = amplitude * np.sin(phase_shift)
        yield value
        phase_shift = np.around((phase_shift + phase_angle) % (2*np.pi), decimals=15)
