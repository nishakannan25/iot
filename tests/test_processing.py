from processing.data_processor import process_data

def test_processing():
    data = {
        "temperature": 30,
        "humidity": 60
    }

    assert process_data(data) == 45