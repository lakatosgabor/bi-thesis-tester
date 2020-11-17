from selenium import webdriver
import unittest
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    a="http://127.0.0.1:8000"

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser=webdriver.Firefox()
        cls.browser.implicitly_wait(10)
        cls.browser.maximize_window()

    def test_browser(self):
        self.browser.get(self.a)

    def test_unsuccess_login(self):
        #sikertelen bejelentkezési folyamat
        self.browser.find_element_by_name("email").send_keys("ele@gmail.com")
        self.browser.find_element_by_name("password").send_keys("allgato")
        self.browser.find_element_by_name("login").click()

    def test_success_login(self):
        #sikeres bejelentkezés folyamat
        self.browser.find_element_by_name("email").send_keys("elek@gmail.com")
        self.browser.find_element_by_name("password").send_keys("hallgato")
        self.browser.find_element_by_name("login").click()


    def test_tearDownClass(cls) -> None:
        cls.browser.close()
        cls.browser.quit()
        print("Test Completed")



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/lakatosgabor/PycharmProjects/bi-thesis-tester'))


