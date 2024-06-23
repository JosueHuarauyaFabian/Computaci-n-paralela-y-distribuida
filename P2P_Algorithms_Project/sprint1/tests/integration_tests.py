import sys
import os
import unittest

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from gather_client import GatherClient
from gather_server import GatherServer

class TestGather(unittest.TestCase):
    def test_gather_data(self):
        server = GatherServer()
        client1 = GatherClient(node_id=1)
        client2 = GatherClient(node_id=2)
        data1 = "Data from node 1"
        data2 = "Data from node 2"

        # Enviar datos al servidor
        client1.send_data(data1)
        client2.send_data(data2)

        # Recibir datos en el servidor
        received_data1 = server.receive_data()
        received_data2 = server.receive_data()

        # Verificar que los datos recibidos sean correctos
        self.assertEqual(received_data1, data1)
        self.assertEqual(received_data2, data2)

if __name__ == '__main__':
    unittest.main()
