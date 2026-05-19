import pytest
import os
import time
import allure

from pytest_html import extras
from utils.driver_manager import DriverManager
from datetime import datetime


# =========================
# RUN ID FOR LOGS
# =========================

if "RUN_ID" not in os.environ:

    os.environ["RUN_ID"] = (
        datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )
    )


# =========================
# AUTO LOGGER
# =========================

@pytest.fixture(autouse=True)
def test_logger():

    print("\n=== Test Started ===")

    yield

    print("\n=== Test Finished ===")


# =========================
# CUSTOM CLI OPTIONS
# =========================

def pytest_addoption(parser):

    parser.addoption(

        "--browser",

        action="store",

        default="chrome",

        help="Browser to run tests"
    )

    parser.addoption(

        "--headless",

        action="store_true",

        help="Run browser in headless mode"
    )

    parser.addoption(

        "--env",

        action="store",

        default="qa",

        help="Environment to run tests"
    )


# =========================
# ENV SETUP
# =========================

@pytest.fixture(
    scope="session",
    autouse=True
)

def set_env(request):

    env = request.config.getoption(
        "--env"
    )

    os.environ["TEST_ENV"] = env


# =========================
# DRIVER FIXTURE
# =========================

@pytest.fixture(scope="function")

def driver(request):

    browser = request.config.getoption(
        "--browser"
    )

    headless = request.config.getoption(
        "--headless"
    )

    driver = DriverManager.get_driver(
        browser,
        headless
    )

    yield driver

    driver.quit()


# =========================
# SCREENSHOTS ON FAILURE
# =========================

@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    extra = getattr(report, "extras", [])

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        os.makedirs(
            "screenshots",
            exist_ok=True
        )

        worker = os.getenv(
            "PYTEST_XDIST_WORKER",
            "main"
        )

        filename = (

            f"screenshots/"
            f"{worker}_"
            f"{item.name}_"
            f"{int(time.time())}.png"
        )

        driver.save_screenshot(filename)

        allure.attach.file(

            filename,

            name="Failure Screenshot",

            attachment_type=
            allure.attachment_type.PNG
        )

        extra.append(
            extras.image(filename)
        )

        print(
            f"\nScreenshot saved: {filename}"
        )

    report.extras = extra