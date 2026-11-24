
# IoT Sensor Data Analysis using NumPy

import numpy as np

# Temperature sensor readings
readings = np.array([25, 27, 26, 29, 30, 28, 27, 31, 29, 26])

print("Sensor Readings:", readings)

print("Mean:", np.mean(readings))
print("Median:", np.median(readings))
print("Minimum:", np.min(readings))
print("Maximum:", np.max(readings))
print("Standard Deviation:", round(np.std(readings), 2))

# Threshold analysis
threshold = 28

high_readings = readings[readings > threshold]

print("Readings above threshold:", high_readings)
print("Number of high readings:", len(high_readings))
