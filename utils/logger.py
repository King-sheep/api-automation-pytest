# @Author: Sheep Wang
# @File: logger.py
# @Created: 2026-09-07 20:38
# @Description: logger.py



import logging
import os
from datetime import datetime




def get_logger(name: str = "API_Test"):
    """
    Creates and manages a logger instance.
    Logs messages to both console and log files under logs/ directory.
    """
    logger = logging.getLogger(name)

    # Avoid adding duplicate handlers if logger is already configured
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # Define log format
    formatter = logging.Formatter(
        fmt="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 1. Console Handler (Print logs to terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 2. File Handler (Save logs into logs/ directory)
    logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    os.makedirs(logs_dir, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    log_file_path = os.path.join(logs_dir, f"test_{today}.log")

    file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


# Global logger instance for easy importing
log = get_logger()