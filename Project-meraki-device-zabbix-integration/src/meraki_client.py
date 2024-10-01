import meraki
from src.utils import load_config, log

def get_meraki_devices(network_id):
    config = load_config()
    dashboard = meraki.DashboardAPI(config['meraki_api_key'])
    
    try:
        # Fetch devices from the specified network
        devices = dashboard.networks.getNetworkDevices(network_id)
        log(f"Fetched {len(devices)} devices from Meraki network {network_id}")
        return devices
    except Exception as e:
        log(f"Error fetching Meraki devices: {e}", level='error')
        return []

# Fetch additional device details if needed
def get_device_details(serial):
    config = load_config()
    dashboard = meraki.DashboardAPI(config['meraki_api_key'])
    
    try:
        device_detail = dashboard.devices.getDevice(serial)
        log(f"Fetched details for device with serial {serial}")
        return device_detail
    except Exception as e:
        log(f"Error fetching device details for serial {serial}: {e}", level='error')
        return {}
