import requests

def test_add_node():
    response = requests.post("http://127.0.0.1:5000/add_node", json={"address": "127.0.0.1:5557"})
    assert response.status_code == 200
    data = response.json()
    assert data['success'] == True

def test_get_metrics():
    response = requests.get("http://127.0.0.1:5000/metrics/metrics")
    assert response.status_code == 200
    data = response.json()
    assert 'latency' in data
    assert 'bandwidth' in data

if __name__ == "__main__":
    test_add_node()
    test_get_metrics()
    print("Todas las pruebas de integración pasaron!")
