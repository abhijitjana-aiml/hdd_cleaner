import os

def is_mounted(path: str) -> bool:
    """Check if HDD is mounted."""
    return os.path.ismount(path)
