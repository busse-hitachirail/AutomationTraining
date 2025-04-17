import logging
import os

def pytest_configure(config):
    """
    Configure logging before any tests run.
    """
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename="logs/test.log",
        format="%(asctime)s %(levelname)s: %(message)s",
        level=logging.INFO
    )
    logging.info("===== Test session started =====")
