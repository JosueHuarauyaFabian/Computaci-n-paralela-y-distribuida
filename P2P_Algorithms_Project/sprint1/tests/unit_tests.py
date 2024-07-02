import sys
import os
import unittest

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from broadcast_client import BroadcastClient

class TestBroadcastClient(unittest.TestCase):
    def test_broadcast_message(self):
        client = BroadcastClient()
        message = "Hello to all nodes"
        client.broadcast_message(message)
        self.assertEqual(client.last_message, message)

if __name__ == '__main__':
    unittest.main()
