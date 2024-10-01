import unittest
from src.meraki_client import get_meraki_devices
from src.zabbix_client import connect_to_zabbix

class TestMerakiToZabbix(unittest.TestCase):

    def test_get_meraki_devices(self):
        devices = get_meraki_devices()
        self.assertIsInstance(devices, list)

    def test_zabbix_connection(self):
        zapi = connect_to_zabbix()
        self.assertIsNotNone(zapi)

if __name__ == '__main__':
    unittest.main()
