import numpy as np
import time
import random

class PPGSimulator:
    """
    Simulates a PPG waveform for heart rate & SpO2 extraction.
    Produces realistic pulse shapes with noise & motion artifacts.
    """

    def __init__(self, heart_rate=75, spo2=98, noise_level=0.02):
        self.heart_rate = heart_rate
        self.spo2 = spo2
        self.noise_level = noise_level
        self.t = 0.0
        self.dt = 1.0 / 100.0  # 100 Hz sampling

    def _simulate_ppg_wave(self):
        # Basic heartbeat sinusoid
        freq = self.heart_rate / 60.0
        base = 0.5 * (1 + np.sin(2 * np.pi * freq * self.t))

        # Add sharper systolic peak
        peak = 0.3 * np.exp(-((self.t * freq * 10) % 1) * 8)

        # Add some physiological variability
        variability = 0.01 * np.sin(2 * np.pi * 0.1 * self.t)

        # Final clean PPG signal
        signal = base + peak + variability
        return signal

    def read(self):
        clean = self._simulate_ppg_wave()

        # Motion artifact noise
        motion_noise = self.noise_level * random.uniform(-1.5, 1.5)

        # Random ambient light noise
        ambient_noise = self.noise_level * random.uniform(-0.5, 0.5)

        # Combined signal
        noisy = clean + motion_noise + ambient_noise

        self.t += self.dt
        return max(0, noisy)
