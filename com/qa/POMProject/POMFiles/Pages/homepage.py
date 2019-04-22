class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.employeebutton_button_xpath = "//body/div[@id='wrapper']/div[@id='sidebar']/div[@class='sidenav']/div[@class='mainnav']/ul/li[9]/a[1]"
        self.viewemployee_button_xpath = "//a[contains(text(),'View Employee')]"
        self.addemployee_button_xpath = "//button[contains(text(),'Add Employee')]"
        self.firstname_textbox_id = "at_emp_fname"
        self.lastname_textbox_id = "at_emp_lname"
        self.gender_button_xpath = "//body//label[2]"
        self.jobtitle_textbox_id = "at_emp_jt_id"
        self.department_textbox_id = "at_emp_dept_id"
        self.birthdate_textbox_id = "mask-date"
        self.contactnumber_textbox_id = "at_emp_phone"
        self.emailid_textbox_id = "at_emp_email"
        self.joiningdate_textbox_id = "mask-date2"
        self.username_textbox_id = "at_emp_username"
        self.password_textbox_id = "at_emp_password"
        self.uploadimage_button_id = "at_emp_profileImg"
        self.uploadimagevalue_textbox_id = "at_emp_profileImg"
        self.addbutton_button_id = "btnAdd"


        self.studentfees_button_xpath = "//body/div/div/div[@class='sidenav']/div[@class='mainnav']/ul/li[13]/a[1]"
        self.listofassignedfees_button_xpath = "//a[contains(text(),'List Assigned Fees')]"
        self.addcoursefees_button_xpath = "//button[contains(text(),'Add Course Fees')]"
        self.courseofschool_button_xapth = "//span[contains(text(),'Select Course')]"
        self.selectcourse_textbox_xpath = "//div[@class='select2-search']//input[@type='text']"
        self.entercoursevalue_textbox_xpath = "//div[@class='select2-search']//input[@type='text']"
        self.streamunder_textbox_id = "at_str_name"
        self.feesname_textbox_id = "at_fs_name"
        self.assignfeesvalue_textbox_id = "at_fs_value"
        self.duedate_textbox_id = "at_fa_lastdate"
        self.fine_textbox_id = "at_fa_fine_percent"
        self.finedropdown_textbox_id = "at_fa_fine_rate"
        self.add_button_id = "btnAdd"

        self.holidays_button_xpath= "//body/div[@id='wrapper']/div[@id='sidebar']/div[@class='sidenav']/div[@class='mainnav']/ul/li[6]/a[1]"
        self.viewholidays_button_xpath = "//a[contains(text(),'View Holidays')]"
        self.addholidays_button_xpath = "//button[contains(text(),'Add Holidays')]"
        self.occasionname_textbox_id = "at_hl_name"
        self.from_button_id = "at_hl_fromDate"
        self.date_button_xpath = "//a[contains(text(),'13')]"
        self.to_button_id = "at_hl_toDate"
        self.todate_button_xpath = "//a[contains(text(),'30')]"
        self.submit_button_id = "btnAdd"

        self.examination_button_xpath = "//body/div[@id='wrapper']/div[@id='sidebar']/div[@class='sidenav']/div[@class='mainnav']/ul/li[16]/a[1]"
        self.examtype_button_xpath = "//a[contains(text(),'Exam Type')]"
        self.addemployee1_button_xpath = "//a[contains(text(),'Add Employee')]"
        self.examtype_textbox_id = "at_extyp_type"
        self.save_button_xpath = "//button[contains(text(),'Save')]"
        self.cancelbutton_button_xpath = "//button[contains(text(),'×')]"

        # self.stream_button_xpath = "//li[@class='active open']//a[@class='hasUl']"
        # self.viewstream_button_xpath = "//a[@class='current']"
        # self.delete_button_xpath = "//span[@id='btn_disp_3']//a[@title='Delete']"

        # self.delete_button_xpath = "//tr[1]//td[2]//span[1]//a[2]"

        self.subject1_button_xpath = ".//*[@id='sidebar']/div[2]/div[2]/ul/li[4]/a"
        self.viewsubject_button_xpath = ".//*[@id='sidebar']/div[2]/div[2]/ul/li[4]/ul/li/a"
        self.save1_button_xpath = "//a[@id='ToolTables_DataTables_Table_0_2']"
        self.excel_textbox_xpath = "//embed[@id='ZeroClipboard_TableToolsMovie_3']"
        self.save2_button_xpath = "//a[@id='ToolTables_DataTables_Table_0_2']"
        self.excel2_textbox_xpath = "//embed[@id='ZeroClipboard_TableToolsMovie_3']"
        # self.pdf_textbox_id = "ZeroClipboard_TableToolsMovie_4"

    def click_employeebutton(self):
        self.driver.find_element_by_xpath(self.employeebutton_button_xpath).click()

    def click_viewemployee(self):
        self.driver.find_element_by_xpath(self.viewemployee_button_xpath).click()

    def click_addemployee(self):
        self.driver.find_element_by_xpath(self.addemployee_button_xpath).click()

    def enter_firstname(self, name):
        self.driver.find_element_by_id(self.firstname_textbox_id).send_keys(name)

    def enter_lastname(self , lastname):
        self.driver.find_element_by_id(self.lastname_textbox_id).send_keys(lastname)

    def click_gender(self):
        self.driver.find_element_by_xpath(self.gender_button_xpath).click()

    def enter_jobtitle(self,title):
        self.driver.find_element_by_id(self.jobtitle_textbox_id).send_keys(title)

    def enter_department(self,value):
        self.driver.find_element_by_id(self.department_textbox_id).send_keys(value)

    def enter_birthdate(self,date):
        self.driver.find_element_by_id(self.birthdate_textbox_id).send_keys(date)

    def enter_contactnumber(self,number):
        self.driver.find_element_by_id(self.contactnumber_textbox_id).send_keys(number)

    def enter_emailid(self,id):
        self.driver.find_element_by_id(self.emailid_textbox_id).send_keys(id)

    def enter_joiningdate(self,joining):
        self.driver.find_element_by_id(self.joiningdate_textbox_id).send_keys(joining)

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_uploadimage(self):
        self.driver.find_element_by_id(self.uploadimage_button_id).click()

    def enter_uploadimagevalue(self, imagevalue):
        self.driver.find_element_by_id(self.uploadimagevalue_textbox_id).send_keys(imagevalue)

    def click_addbutton(self):
        self.driver.find_element_by_id(self.addbutton_button_id).click()

    def click_studentfees(self):
        self.driver.find_element_by_xpath(self.studentfees_button_xpath).click()

    def click_assignedfees(self):
        self.driver.find_element_by_xpath(self.listofassignedfees_button_xpath).click()

    def click_coursefees(self):
        self.driver.find_element_by_xpath(self.addcoursefees_button_xpath).click()

    def click_school(self):
        self.driver.find_element_by_xpath(self.courseofschool_button_xapth).click()

    def enter_selectcourse(self, course):
        self.driver.find_element_by_xpath(self.selectcourse_textbox_xpath).send_keys(course)

    def enter_coursevalue(self, value):
        self.driver.find_element_by_xpath(self.entercoursevalue_textbox_xpath).send_keys(value)

    def enter_stream(self, stream):
        self.driver.find_element_by_id(self.streamunder_textbox_id).send_keys(stream)

    def enter_fees(self,feesname ):
        self.driver.find_element_by_id(self.feesname_textbox_id).send_keys(feesname)

    def enter_assignfees(self, fees):
        self.driver.find_element_by_id(self.assignfeesvalue_textbox_id).send_keys(fees)

    def enter_duedate(self, date):
        self.driver.find_element_by_id(self.duedate_textbox_id).send_keys(date)

    def enter_fine(self, fine):
        self.driver.find_element_by_id(self.fine_textbox_id).send_keys(fine)

    def enter_finedropdown(self, dropdown):
        self.driver.find_element_by_id(self.finedropdown_textbox_id).send_keys(dropdown)

    def click_add(self):
        self.driver.find_element_by_id(self.add_button_id).click()

    def click_holidays(self):
        self.driver.find_element_by_xpath(self.holidays_button_xpath).click()

    def click_viewholidays(self):
        self.driver.find_element_by_xpath(self.viewholidays_button_xpath).click()

    def click_addholidays(self):
        self.driver.find_element_by_xpath(self.addholidays_button_xpath).click()

    def enter_occasion(self,occasionname):
        self.driver.find_element_by_id(self.occasionname_textbox_id).send_keys(occasionname)

    def click_from(self):
        self.driver.find_element_by_id(self.from_button_id).click()

    def click_fromdate(self):
        self.driver.find_element_by_xpath(self.date_button_xpath).click()

    def click_to(self):
        self.driver.find_element_by_id(self.to_button_id).click()

    def click_todate(self):
        self.driver.find_element_by_xpath(self.todate_button_xpath).click()

    def click_submit(self):
        self.driver.find_element_by_id(self.submit_button_id).click()

    def click_examination(self):
        self.driver.find_element_by_xpath(self.examination_button_xpath).click()

    def click_examtype(self):
        self.driver.find_element_by_xpath(self.examtype_button_xpath).click()

    def click_addemployee1(self):
        self.driver.find_element_by_xpath(self.addemployee1_button_xpath).click()

    def enter_examtype1(self, type):
        self.driver.find_element_by_id(self.examtype_textbox_id).send_keys(type)

    def click_savebtn(self):
        self.driver.find_element_by_xpath(self.save_button_xpath).click()

    def click_cancel(self):
        self.driver.find_element_by_xpath(self.cancelbutton_button_xpath).click()

    # def click_stream(self):
    #     self.driver.find_element_by_xpath(self.stream_button_xpath).click()
    #
    # def click_viewstream(self):
    #     self.driver.find_element_by_xpath(self.viewstream_button_xpath).click()
    #
    # def click_delete(self):
    #     self.driver.find_element_by_xpath(self.delete_button_xpath).click()

    def click_subject1(self):
        self.driver.find_element_by_xpath(self.subject1_button_xpath).click()

    def click_viewsubject(self):
        self.driver.find_element_by_xpath(self.viewsubject_button_xpath).click()

    def click_savebutton1(self):
        self.driver.find_element_by_xpath(self.save1_button_xpath).click()

    def click_excelbutton(self):
        self.driver.find_element_by_xpath(self.excel_textbox_xpath).click()

    def click_savebutton2(self):
        self.driver.find_element_by_xpath(self.save2_button_xpath).click()

    def click_excelbutton2(self):
         self.driver.find_element_by_xpath(self.excel2_textbox_xpath).click()

