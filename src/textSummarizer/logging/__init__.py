import os
import sys
import logging

logging_string = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_directory = "logs"
log_path = os.path.join(log_directory,"running_logs.log")
os.makedirs(log_directory, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_string,
    
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")