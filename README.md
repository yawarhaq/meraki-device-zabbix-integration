Overview: 

- This project provides a seamless integration between Cisco Meraki and Zabbix, allowing users to automatically fetch device information from Meraki's dashboard and add it to their Zabbix monitoring system. By leveraging the Meraki API, the integration collects essential device data such as serial numbers, models, and IP addresses, and updates the Zabbix server accordingly. This enhances network monitoring capabilities, enabling administrators to have a centralized view of their network devices.

Features:

- Automatic Device Discovery: Fetches all devices from specified Meraki networks and organizations.
- Detailed Device Information: Collects comprehensive device details, including model, serial number, MAC address, and IP address.
- Zabbix Integration: Adds devices to Zabbix with relevant information, including host and interface configurations.
- Logging: Maintains detailed logs of operations to monitor the integration's performance and troubleshoot issues.

Technologies Used:

- Python: The primary programming language for developing the integration.
- Meraki Dashboard API: Used for interacting with Meraki devices and fetching their details.
- Zabbix API: Utilized to add devices to the Zabbix monitoring system.
- Logging: Built-in Python logging module to track actions and errors.
