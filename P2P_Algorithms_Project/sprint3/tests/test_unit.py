import zlib

def test_compression():
    data = "test data"
    compressed_data = zlib.compress(data.encode())
    decompressed_data = zlib.decompress(compressed_data).decode()
    assert decompressed_data == data

def test_data_structure():
    data = {
        "latency": 50,
        "bandwidth": 50,
        "nodes": []
    }
    assert 'latency' in data
    assert 'bandwidth' in data
    assert isinstance(data['nodes'], list)

if __name__ == "__main__":
    test_compression()
    test_data_structure()
    print("Todas las pruebas unitarias pasaron!")
