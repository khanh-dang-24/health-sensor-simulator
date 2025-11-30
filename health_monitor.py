import csv
import time
from datetime import datetime
from ppg_sim import PPGSimulator
import numpy as np

class HealthMonitor:
    def __init__(self, sample_rate=100):
        self.sample_rate = sample_rate
        self.buffer = []
        self.timestamps = []

    def detect_peaks(self, data):
        peaks = []
        for i in range(1, len(data)-1):
            if data[i] > data[i-1] and data[i] > data[i+1] and data[i] > np.mean(data)*1.1:
                peaks.append(i)
        return peaks

    def compute_heart_rate(self, peaks):
        if len(peaks) < 2:
            return None
        intervals = [(peaks[i] - peaks[i-1]) / self.sample_rate for i in range(1, len(peaks))]
        avg_interval = sum(intervals) / len(intervals)
        return round(60.0 / avg_interval)

    def compute_spo2(self, signal):
        return round(97 + (np.std(signal) * 3), 1)

def run(duration=20, csv_path="ppg_data.csv"):
    sim = PPGSimulator()
    monitor = HealthMonitor(sample_rate=100)

    print("Starting PPG Health Monitor Simulation...\n")
    print("Time\t\tHeart Rate (BPM)\tSpO2 (%)")

    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "heart_rate_bpm", "spo2", "raw_signal"])

        start = time.time()
        while time.time() - start < duration:
            signal = sim.read()
            monitor.buffer.append(signal)

            if len(monitor.buffer) > 300:  # 3 sec window
                window = monitor.buffer[-300:]
                peaks = monitor.detect_peaks(window)
                hr = monitor.compute_heart_rate(peaks)
                spo2 = monitor.compute_spo2(window)

                now = datetime.utcnow().isoformat() + "Z"
                writer.writerow([now, hr, spo2, signal])

                print(f"{now}\t{hr}\t\t\t{spo2}")

            time.sleep(0.01)

if __name__ == "__main__":
    run(duration=20)
