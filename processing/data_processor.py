def process_data(data):
    avg = (data["temperature"] + data["humidity"]) / 2
    return avg