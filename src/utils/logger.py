import logging
import os

LOG_FILE = "data/logs/app.log"

# Ensure logs directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("HDDCleaner")
