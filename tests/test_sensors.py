from sensors.sensor import read_sensor

def test_sensor_connection():
    data = read_sensor()

    assert "temperature" in data
    assert "humidity" in data