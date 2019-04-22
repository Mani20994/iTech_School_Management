from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from com.qa.POMProject.POMFiles.Pages.loginpage import LoginPage
from com.qa.POMProject.POMFiles.Pages.homepage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\Nxt\\PycharmProjects\\POM(Online Food odering)\\Drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get(" http://school.itechscripts.com")

        login = LoginPage(driver)
        login.enter_username("school")
        login.enter_password("schoolp")
        login.click_login()

        homepage = HomePage(driver)

        homepage.click_employeebutton()
        time.sleep(2)
        homepage.click_viewemployee()
        driver.implicitly_wait(20)
        homepage.click_addemployee()
        driver.implicitly_wait(20)
        homepage.enter_firstname("Nidhi")
        homepage.enter_lastname("Kulkarni")
        homepage.click_gender()
        time.sleep(2)
        homepage.enter_jobtitle("Teachers")
        time.sleep(2)
        homepage.enter_department("Teacher")
        time.sleep(2)
        homepage.enter_birthdate("20/09/2008")
        time.sleep(2)
        homepage.enter_contactnumber("9887755660")
        time.sleep(2)
        homepage.enter_emailid("abc@gmail.com")
        time.sleep(2)
        homepage.enter_joiningdate("25/06/2018")
        time.sleep(2)
        homepage.enter_username("school@")
        time.sleep(2)
        homepage.click_uploadimage()
        time.sleep(2)
        homepage.enter_uploadimagevalue("C:\\Users\\Nxt\\Pictures\\Admin association.PNG")
        time.sleep(5)
        homepage.click_addbutton()
        time.sleep(2)

        homepage.click_studentfees()
        time.sleep(2)
        homepage.click_assignedfees()
        time.sleep(2)
        homepage.click_coursefees()
        time.sleep(2)
        homepage.click_school()
        time.sleep(2)
        homepage.enter_selectcourse("Lower Nursery")
        time.sleep(2)
        homepage.enter_coursevalue(Keys.ENTER)
        time.sleep(2)
        homepage.enter_stream("Science")
        time.sleep(2)
        homepage.enter_fees("Admission fee")
        time.sleep(2)
        homepage.enter_assignfees("1000")
        time.sleep(2)
        homepage.enter_duedate("June")
        time.sleep(2)
        homepage.enter_fine("500")
        time.sleep(2)
        homepage.enter_finedropdown("Per Month")
        time.sleep(2)
        homepage.click_add()
        time.sleep(5)

        homepage.click_holidays()
        homepage.click_viewholidays()
        time.sleep(2)
        homepage.click_addholidays()
        time.sleep(2)
        homepage.enter_occasion("Summer Holidays")
        time.sleep(2)
        homepage.click_from()
        time.sleep(4)
        homepage.click_fromdate()
        time.sleep(4)
        homepage.click_to()
        time.sleep(4)
        homepage.click_todate()
        time.sleep(2)
        homepage.click_submit()

        homepage.click_examination()
        time.sleep(2)
        homepage.click_examtype()
        time.sleep(2)
        homepage.click_addemployee1()
        time.sleep(5)
        homepage.enter_examtype1("annual")
        time.sleep(3)
        homepage.click_savebtn()
        time.sleep(3)
        homepage.click_cancel()
        time.sleep(5)

        # homepage.click_delete()
        # time.sleep(2)
        # driver.switch_to.alert.accept()
        # time.sleep(2)
        # homepage.enter_password("school1234")

        homepage.click_subject1()
        time.sleep(2)
        homepage.click_viewsubject()
        time.sleep(2)
        homepage.click_savebutton1()
        time.sleep(2)
        homepage.click_excelbutton()
        time.sleep(10)
        homepage.click_savebutton2()
        time.sleep(2)
        homepage.click_excelbutton2()
        time.sleep(2)




    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()
    #     print("Test Completed")


if __name__ == '__main__':
    unittest.main()

