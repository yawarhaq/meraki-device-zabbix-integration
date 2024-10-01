import json
import logging

# Load configuration from config.json
def load_config():
    with open('config/config.json') as config_file:
        return json.load(config_file)

# Set up logging
def setup_logging():
    logging.basicConfig(filename='logs/app.log', level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

def log(message, level='info'):
    if level == 'info':
        logging.info(message)
    elif level == 'error':
        logging.error(message)
