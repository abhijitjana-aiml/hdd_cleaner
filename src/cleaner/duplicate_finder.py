import hashlib
import os
from utils.file_utils import get_all_files
from utils.logger import logger

class DuplicateFinder:

    def __init__(self, base_path: str):
        self.base_path = base_path

    def remove_duplicates(self):
        logger.info("Checking for duplicate files...")

        seen = {}
        files = get_all_files(self.base_path)

        for f in files:
            file_hash = self.hash_file(f)

            if file_hash in seen:
                logger.info(f"Duplicate found: {f}")
                try:
                    os.remove(f)
                except Exception as e:
                    logger.error(f"Error deleting duplicate: {e}")
            else:
                seen[file_hash] = f

        logger.info("Duplicate removal completed.")

    def hash_file(self, path):
        """Return SHA256 hash of file"""
        hasher = hashlib.sha256()
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
