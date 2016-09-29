# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptons import NoSuchElementException


class Docker(unittest.TestCase):

    # setting up browser for test
    # we can chose either one of the browser.With advance codeing we can run both parallaly,or we can chose which browser to run test
    # useing javascript popup(done it in java ,not python).I am not sure if you want me to do that

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.docker.com"
        self.verificationErrors = []
        self.accept_next_alert = True

   # search for any keyword in the search box
# choose it to verify data outcome
    def test_001_search_with_ivalid_keyword(self):
        self.search_docks("dfefevqv")
        self.search_docks_assertion()



   # verify the title of docker website
# It could be our smoke test to see if website is stable to test
    def test__002_Verify_docker_website_title_url(self):

        driver = self.driver
        driver.get(self.base_url)
        title=driver.title
        print(title)
        assert title=="Docker - Build, Ship, and Run Any App, Anywhere"


    # signup to docker website,In an idle test senerio i would have genarated random e-mail but docker might block my ip address if
    # i keep signing up with different e-mail address from same ip.
    # Its one of the most important feature of docker sight
    def test_003_docker_signup(self):

      self.signup("test","test@gmail.com","123456")

    # login to docker website and logout.
    def test_004_login_valid_username_valid_password(self):

        self.login("waseyrabby@gmail.com", "718756Home")
        self.logout()
   # try to login with  invalid credential and verify error massage.
    def test_005_login_ivalid_username_valid_password(self):
        self.login("waseyray", "718756Home")
        self.assert_error_massage()

    # try to login with  invalid credential and verify error massage.
    def test_006_login_valid_username_ivalid_password(self):
        self.login("waseyrabby@gmail.com", "12345678")
        self.assert_error_massage()

    # try to login with  invalid credential and verify error massage.
    def test_007_login_ivalid_username_ivalid_password(self):
        self.login("waseyrabbycom", "7187me")
        self.assert_error_massage()

    # click on download link and verify if download link is valid.
    # I choose it because its important that we get new user and we only make money when they sign up and they wont sign up
    # if the begening is not stable(download link broken)


    def test_008_download_mac_link(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_css_selector("li.leaf.menu-mlid-954 > a").click()
        driver.find_element_by_link_text("Learn More").click()
        driver.find_element_by_link_text("Download Docker for Mac").click()

    def signup(self,user,e_mail,pasword):

        driver = self.driver
        driver.get(self.base_url)
        signup=driver.find_element_by_xpath("html/body/div[1]/div/header/div[3]/div/div[2]/ul[1]/li[9]/a")
        signup.click()
        self.driver.switch_to.window(window_name=self.driver.window_handles[-1])
        username=driver.find_element_by_name("username")
        username.send_keys(user)
        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys(e_mail)
        password = driver.find_element_by_name("password")
        password.clear()
        password.send_keys(pasword)
        submit = driver.find_element_by_xpath("//button[@type='submit']")
        submit.click()

    def assert_error_massage(self):
        error = self.driver.find_element_by_css_selector(".styles__error___2FnCO")
        errormassage = error.text
        assert errormassage=="Incorrect authentication credentials."



    def login(self, username, passowrd):
        """

         :return:
          """
        driver = self.driver
        driver.get(self.base_url)
        login = driver.find_element_by_xpath("html/body/div[1]/div/header/div[3]/div/div[2]/ul[1]/li[8]/a")
        login.click()
        self.driver.switch_to.window(window_name=self.driver.window_handles[-1])
        dockerid = driver.find_element_by_id("mui-id-0")
        dockerid.clear()
        dockerid.send_keys(username)
        dockerpassword = driver.find_element_by_id("mui-id-1")
        dockerpassword.clear()
        dockerpassword.send_keys(passowrd)
        submitlogin = driver.find_element_by_xpath(".//*[@id='root']/div/div/div/div/div[2]/div/form/button")
        submitlogin.click()

    def logout(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='layout-main']/div/header/div/div/div[3]/button").click()
        driver.find_element_by_css_selector("div.styles__logout___2VxPp").click()

    def search_docks(self, search):
        driver = self.driver
        driver.get(self.base_url)
        docks = driver.find_element_by_xpath("(//a[contains(text(),'Docs')])[2]")
        docks.click()
        self.driver.switch_to.window(window_name=self.driver.window_handles[-1])
        searchbox = driver.find_element_by_id("st-search-input")
        searchbox.clear()
        searchbox.send_keys(search)
        driver.find_element_by_xpath("//button[@type='submit']").click()



    def search_docks_assertion(self):
        noresult = self.driver.find_element_by_css_selector(".ais-hits.ais-hits__empty")
        output = noresult.text
        assert output == "No results"


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


# after test closeing the browser.
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
