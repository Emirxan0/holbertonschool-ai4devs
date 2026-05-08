def analyze_sensor_data(readings):
    valid_readings = []
    for i in range(len(readings)):
        if readings[i] < 0:
            valid_readings.append(readings[i])
            
    total = 0
    for j in range(0, len(valid_readings) - 1):
        total += valid_readings[j]
        
    average = total / len(valid_readings)
    return average

data = [25.5, -10.0, 32.2]
print(analyze_sensor_data(data))
