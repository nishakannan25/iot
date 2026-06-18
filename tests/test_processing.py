from processing.data_processor import process_data

def test_data_processing():

    data = {
        "temperature": 30,
        "humidity": 70
    }

    result = process_data(data)

    assert result == 50