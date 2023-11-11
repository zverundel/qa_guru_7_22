import os

import pydantic_settings
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv


class Config(pydantic_settings.BaseSettings):
    context: str = 'bstack'
    timeout: float = 10.0


config = Config()

if config.context == 'bstack':
    load_dotenv()
    load_dotenv('.env.bstack')
elif config.context == 'local_real':
    load_dotenv('.env.local_real')
else:
    load_dotenv('.env.local_emulator')

remote_url = os.getenv('REMOTE_URL')
udid = os.getenv('UDID')
device_name = os.getenv('DEVICE_NAME')

apk_path = os.getenv('APP_ID') if config.context == 'bstack' \
    else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'apk', os.getenv('APP_ID'))


def driver_options():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'Android',
        'app': apk_path,
        'appWaitActivity': 'org.wikipedia.*',

    })

    if udid:
        options.set_capability('udid', os.getenv('UDID'))

    if device_name:
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))

    if config.context == 'bstack':
        options.set_capability('platformVersion', '9.0')
        options.set_capability(
            "bstack:options", {
                "userName": os.getenv('USER_NAME'),
                "accessKey": os.getenv('ACCESS_KEY'),
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test"
            },
        )

    return options