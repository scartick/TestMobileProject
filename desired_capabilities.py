import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def get_desired_capabilities(app):
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '12.0',
        'deviceName': 'iPhone X',
        'automationName': 'XCUITest',
        'app': PATH('./app/' + app),
    }

    return desired_caps