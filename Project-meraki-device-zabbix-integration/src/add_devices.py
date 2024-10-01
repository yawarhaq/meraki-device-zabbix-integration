from src.meraki_client import get_meraki_devices, get_device_details
from src.zabbix_client import connect_to_zabbix, add_device_to_zabbix
from src.utils import setup_logging, log, load_config

def add_meraki_devices_to_zabbix():
    # Set up logging
    setup_logging()
    
    # Load the network ID from the config
    config = load_config()
    network_id = config['meraki_network_id']
    
    # Fetch devices from Meraki
    devices = get_meraki_devices(network_id)
    
    # Connect to Zabbix
    zapi = connect_to_zabbix()
    
    # Add devices to Zabbix
    for device in devices:
        serial = device.get('serial')
        if not serial:
            log(f"Skipping device {device['name']} as it has no serial number", level='error')
            continue
        
        # Fetch device details from Meraki
        device_details = get_device_details(serial)
        
        # Add the device and its details to Zabbix
        add_device_to_zabbix(zapi, device, device_details)
    
    log("Finished adding devices to Zabbix")
