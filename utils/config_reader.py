import json
import os


def load_config():

    env = os.getenv(
        "TEST_ENV",
        "qa"
    )

    with open(
        "config/config.json"
    ) as f:

        all_config = json.load(f)

    return all_config[env]