from utils.hdd_utils import is_mounted
from cleaner.file_cleaner import FileCleaner
from cleaner.duplicate_finder import DuplicateFinder
from image_processor.face_cluster import FaceCluster

HDD_PATH = "/mnt/myhdd"

def main():
    print("📁 HDD Cleaner Started...")

    if not is_mounted(HDD_PATH):
        print(f"❌ HDD not mounted at {HDD_PATH}")
        return
    else:
        print("✅ HDD is mounted")

    # Step 1: Clean files
    cleaner = FileCleaner(HDD_PATH)
    cleaner.clean()

    # Step 2: Remove duplicates
    dup = DuplicateFinder(HDD_PATH)
    dup.remove_duplicates()

    # Step 3: Cluster images by faces (future expansion)
    cluster = FaceCluster(HDD_PATH)
    cluster.cluster()

    print("✅ All tasks completed successfully.")


if __name__ == "__main__":
    main()
