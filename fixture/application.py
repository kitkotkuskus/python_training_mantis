from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper
from selenium import webdriver


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
        # self.config = config
        self.project = ProjectHelper(self)
        # self.base_url = config['web']['baseUrl']
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        # self.baseUrl = config['web']['baseUrl']
        self.config = config
        self.baseUrl = config['web']['baseUrl']

    def open_home_page(self):
        # open home page
        wd = self.wd
        wd.get(self.baseUrl)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()