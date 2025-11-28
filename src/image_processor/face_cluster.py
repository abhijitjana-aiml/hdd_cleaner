from utils.logger import logger

class FaceCluster:

    def __init__(self, base_path: str):
        self.base_path = base_path

    def cluster(self):
        """
        Placeholder for face clustering functionality.
        Later, you can integrate:
        - face_recognition
        - OpenCV
        - deepface
        """
        logger.info("Face clustering skipped (placeholder).")
        print("⚠ Face clustering feature is not implemented yet.")
