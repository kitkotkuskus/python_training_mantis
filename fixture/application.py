from selenium import webdriver
from python_training_mantis.fixture.session import SessionHelper
from python_training_mantis.fixture.project import ProjectHelper
from python_training_mantis.fixture.james import JamesHelper
from python_training_mantis.fixture.signup import SignupHelper
from python_training_mantis.fixture.mail import MailHelper
from python_training_mantis.fixture.soap import SoapHelper


class Application:

    def __init__(self, browser, config):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.config = config
        self.project = ProjectHelper(self)
        self.base_url = config['web']['baseUrl']
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        # open home page
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()