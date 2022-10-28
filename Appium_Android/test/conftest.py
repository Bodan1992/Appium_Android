import allure_commons
import pytest
from selene.support.shared import browser
from selene import support
from appium import webdriver
from Appium_Android import config
from Appium_Android.util import attachment
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def auto_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def attach_video():
    yield


@pytest.fixture(scope='function', autouse=True)
def create_driver(request):
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )

    yield

    session_id = browser.driver.session_id

    attachment.add_video(session_id, 'Video test')

    attachment.screenshot(name='Last screenshot')
    attachment.screen_xml_dump()

    browser.quit()
