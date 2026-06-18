from sensors.sensor import read_sensor
from processing.data_processor import process_data

def test_complete_flow():
    data = read_sensor()
    result = process_data(data)

    assert result > 0