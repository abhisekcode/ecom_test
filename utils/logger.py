import logging
import os
# from conftest import RUN_ID

# timestamp = datetime.now().strftime(
#     "%Y-%m-%d_%H-%M-%S"
# )

RUN_ID = os.getenv("RUN_ID")
log_dir = f"logs/{RUN_ID}"

os.makedirs(
    log_dir,
    exist_ok=True
)

def get_logger():

    logger = logging.getLogger(
        "framework"
    )

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        os.makedirs(
            "logs",
            exist_ok=True
        )

        formatter = logging.Formatter(
            "%(asctime)s - "
            "%(levelname)s - "
            "%(message)s"
        )

        # Console handler

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(
            formatter
        )

        # File handler

        # file_handler = logging.FileHandler(
        #     "logs/framework.log"
        # )
        worker = os.getenv(
            "PYTEST_XDIST_WORKER",
            "main"
        )

        log_file = (
            f"{log_dir}/{worker}.log"
        )

        file_handler = logging.FileHandler(
            log_file
        )

        file_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            console_handler
        )

        logger.addHandler(
            file_handler
        )

    return logger