from pyzabbix import ZabbixAPI
from src.utils import load_config, log

# Connect to the Zabbix API
def connect_to_zabbix():
    config = load_config()
    zapi = ZabbixAPI(config['zabbix_url'])
    zapi.login(config['zabbix_user'], config['zabbix_password'])
    log("Connected to Zabbix")
    return zapi

def add_device_to_zabbix(zapi, device, device_details):
    config = load_config()
    template_name = config['zabbix_template_name']

    log(f"Adding device to Zabbix: {device['name']} with serial {device['serial']} using template '{template_name}'")

    # Get the template ID by name
    try:
        templates = zapi.template.get({'filter': {'host': template_name}})
        if not templates:
            log(f"Template '{template_name}' does not exist", level='error')
            return
        
        template_id = templates[0]['templateid']
        log(f"Using template ID: {template_id} for device {device['name']}")
    except Exception as e:
        log(f"Error retrieving template ID: {e}", level='error')
        return

    try:
        # Adding host to Zabbix
        response = zapi.host.create({
            'host': device['name'],
            'interfaces': [{
                'type': 1,
                'main': 1,
                'useip': 1,
                'ip': device.get('lanIp', '127.0.0.1'),
                'dns': '',
                'port': '10050'
            }],
            'groups': [{'groupid': config['zabbix_group_id']}],
            'templates': [{'templateid': template_id}],
            'description': f"Model: {device_details.get('model', 'Unknown')} | "
                           f"MAC: {device_details.get('mac', 'Unknown')} | "
                           f"Serial: {device_details.get('serial', 'Unknown')} | "
                           f"Network: {device_details.get('networkId', 'Unknown')}"
        })
        log(f"Added {device['name']} to Zabbix successfully. Response: {response}")
    except Exception as e:
        log(f"Error adding {device['name']} to Zabbix: {e}", level='error')



