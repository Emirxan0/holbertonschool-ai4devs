def analyze_sensor_data(readings):
    if not readings:
        return 0
    
    valid_readings = []
    for i in range(len(readings)):
        if readings[i] >= 0:
            valid_readings.append(readings[i])
            
    if not valid_readings:
        return 0
        
    total = 0
    for j in range(len(valid_readings)):
        total += valid_readings[j]
        
    average = total / len(valid_readings)
    return average

data = [25.5, -10.0, 32.2]
print(analyze_sensor_data(data))
