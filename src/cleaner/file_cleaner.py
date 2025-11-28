import os
from utils.file_utils import get_all_files
from utils.logger import logger

class FileCleaner:

    def __init__(self, base_path: str):
        self.base_path = base_path

    def clean(self):
        logger.info("Starting file cleanup...")

        files = get_all_files(self.base_path)

        for f in files:
            if self.is_corrupt(f):
                logger.info(f"Removing corrupt file: {f}")
                try:
                    os.remove(f)
                except Exception as e:
                    logger.error(f"Failed to remove {f}: {e}")

        logger.info("File cleanup completed.")

    def is_corrupt(self, file_path):
        """
        Dummy corrupt file checker.
        You can replace this with proper validation later.
        """
        if os.path.getsize(file_path) == 0:
            return True
        return False

