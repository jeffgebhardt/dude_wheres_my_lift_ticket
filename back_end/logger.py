import logging

from datetime import datetime

# Set the global format for logging messages
global_formatter = '%(asctime)s-%(levelname)s-%(message)s'

# Create the root logger
logger = logging.getLogger(__name__)

# Write logs to a file in './logs'
logging.basicConfig(filename=f'./logs/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log',
                    format=global_formatter,
                    level=logging.INFO)

# Also output logs to the console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console_formatter = logging.Formatter(global_formatter)
console.setFormatter(console_formatter)
logging.getLogger().addHandler(console)