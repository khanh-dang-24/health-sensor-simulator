# Health Sensor Simulator (PPG, Heart Rate, SpO2)

A high-quality simulation of a **PPG-based health sensor**, similar to the technology used in smartwatches, fitness trackers, and medical wearable devices.  
The simulator generates realistic **heart rate**, **SpO2**, and **photoplethysmography (PPG)** waveforms — including noise, motion artifacts, and physiological variability.

This project runs fully in software (*no hardware required*) and is designed for learning, testing, and showcasing embedded/health-signal processing skills.

---

## 🚀 Features

### ✔ Realistic PPG Waveform Generator
- Systolic peak + dicrotic notch shape  
- Heart rate–based frequency changes  
- Physiological drift & variability  
- Motion artifacts (random disturbances)  
- Ambient light noise  

### ✔ Heart Rate Extraction (BPM)
- Peak detection on PPG waveform  
- Computes beats per minute from inter-peak intervals  
- Sliding analysis window for real-time updates  

### ✔ SpO2 Estimation
- Simplified model using statistical features  
- Noise-aware calculation  

### ✔ Real-Time Terminal Output
Example:
