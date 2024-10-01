Overview
This project provides a seamless integration between Cisco Meraki and Zabbix, allowing users to automatically fetch device information from Meraki's dashboard and add it to their Zabbix monitoring system. By leveraging the Meraki API, the integration collects essential device data such as serial numbers, models, and IP addresses, and updates the Zabbix server accordingly. This enhances network monitoring capabilities, enabling administrators to have a centralized view of their network devices.

Features
Automatic Device Discovery: Fetches all devices from specified Meraki networks and organizations.
Detailed Device Information: Collects comprehensive device details, including model, serial number, MAC address, and IP address.
Zabbix Integration: Adds devices to Zabbix with relevant information, including host and interface configurations.
Logging: Maintains detailed logs of operations to monitor the integration's performance and troubleshoot issues.
Technologies Used
Python: The primary programming language for developing the integration.
Meraki Dashboard API: Used for interacting with Meraki devices and fetching their details.
Zabbix API: Utilized to add devices to the Zabbix monitoring system.
Logging: Built-in Python logging module to track actions and errors.
Getting Started
Prerequisites
Python 3.x
Meraki API Key
Zabbix API URL, username, and password
Installed Python packages: meraki, pyzabbix, and other dependencies from requirements.txt.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/meraki-zabbix-integration.git
cd meraki-zabbix-integration
Install required packages:

bash
Copy code
pip install -r requirements.txt
Configure the integration:

Edit the config/config.json file with your Meraki API key, Zabbix credentials, organization ID, and other necessary parameters.
Running the Integration
Execute the integration script to start fetching devices from Meraki and adding them to Zabbix:

bash
Copy code
python run_integrations.py
Logs
Logs are stored in the logs/app.log file, providing detailed insights into the integration process and any errors encountered.

Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request
