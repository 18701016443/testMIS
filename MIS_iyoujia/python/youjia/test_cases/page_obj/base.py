#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/12/19 11:28
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Pyse(object):
    '''
    PO模型基本类，对原生Selenium进行二次封装。
    '''
    def __init__(self, selenium_driver,canshu):
        self.driver = selenium_driver
        base_url = ["http://testmis.iyoujia.com/#/login", "http://premis.iyoujia.com/#/login","http://mis.iyoujia.com/#/login"]
        if canshu == "test":
            self.base_url = base_url[0]
        if canshu == "pre":
            self.base_url = base_url[1]
        if canshu == "prod":
            self.base_url = base_url[2]
        self.timeout = 30

    def _open(self, url):
        '''
        open the two level path of the bbs
        Usage:
            driver._open(self.base_url+"/index.html")
        '''
        # login_url = self.base_url + "/login.php?"
        url = self.base_url + url
        # self.driver.get(login_url)
        self.driver.get(url)

    def open(self):
        '''
        open bbs index . "https://www.baidu.com"
        Usage:
            driver.open()
        '''
        self._open(self.url)

    def opentest(self,url):
        self.driver.get(url)

    def find_element_format(self, css):
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]
        return by, value

    def element_wait(self, css, secs=None):
        '''
        Waiting for an element to display.
        Usage:
        driver.element_wait("css=>#el",10)
        '''
        by, value = self.find_element_format(css)

        if secs is None:
            secs = self.timeout

        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def get_element(self, css):
        '''
        Judge element positioning way, and returns the element.
        '''
        by, value = self.find_element_format(css)

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def get_elements(self, css):
        '''
        Judge elements positioning way, and returns the elements.
        '''
        by, value = self.find_element_format(css)

        if by == "id":
            elements = self.driver.find_elements_by_id(value)
        elif by == "name":
            elements = self.driver.find_elements_by_name(value)
        elif by == "class":
            elements = self.driver.find_elements_by_class_name(value)
        elif by == "link_text":
            elements = self.driver.find_elements_by_link_text(value)
        elif by == "xpath":
            elements = self.driver.find_elements_by_xpath(value)
        elif by == "css":
            elements = self.driver.find_elements_by_css_selector(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return elements

    def max_window(self):
        '''
        Set browser window maximized.
        Usage:
        driver.max_window()
        '''
        self.driver.maximize_window()

    def set_window(self, wide, high):
        '''
        Set browser window wide and high.
        Usage:
        driver.set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)

    def type(self, css, text):
        '''
        Operation input box.
        Usage:
        driver.type("css=>#el","selenium")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.send_keys(text)

    def clear(self, css):
        '''
        Clear the contents of the input box.
        Usage:
        driver.clear("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.clear()

    def click(self, css):
        '''
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..
        Usage:
        driver.click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.click()

    def right_click(self, css):
        '''
        Right click element.
        Usage:
        driver.right_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, css):
        '''
        Mouse over the element.
        Usage:
        driver.move_to_element("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):
        '''
        Double click element.
        Usage:
        driver.double_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_css, ta_css):
        '''
        Drags an element a certain distance and then drops it.
        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        '''
        self.element_wait(el_css)
        element = self.get_element(el_css)
        self.element_wait(ta_css)
        target = self.get_element(ta_css)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        '''
        Click the element by the link text
        Usage:
        driver.click_text("新闻")
        '''
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        '''
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.
        Usage:
        driver.close()
        '''
        self.driver.close()

    def quit(self):
        '''
        Quit the driver and close all the windows.
        Usage:
        driver.quit()
        '''
        self.driver.quit()

    def submit(self, css):
        '''
        Submit the specified form.
        Usage:
        driver.submit("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.submit()

    def F5(self):
        '''
        Refresh the current page.
        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        '''
        Execute JavaScript scripts.
        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)

    def get_attribute(self, css, attribute):
        '''
        Gets the value of an element attribute.
        Usage:
        driver.get_attribute("css=>#el","type")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.get_attribute(attribute)

    def get_text(self, css):
        '''
        Get element text information.
        Usage:
        driver.get_text("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.text

    def get_display(self, css):
        '''
        Gets the element to display,The return result is true or false.
        Usage:
        driver.get_display("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.is_displayed()

    def get_title(self):
        '''
        Get window title.
        Usage:
        driver.get_title()
        '''
        return self.driver.title

    def get_url(self):
        '''
        Get the URL address of the current page.
        Usage:
        driver.get_url()
        '''
        return self.driver.current_url

    def get_windows_img(self, file_path):
        '''
        Get the current window screenshot.
        Usage:
        driver.get_windows_img()
        '''
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, secs):
        '''
        Implicitly wait.All elements on the page.
        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        '''
        Accept warning box.
        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.
        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        '''
        Switch to the specified frame.
        Usage:
        driver.switch_to_frame("css=>#el")
        '''
        self.element_wait(css)
        iframe_el = self.get_element(css)
        self.driver._switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver._switch_to.default_content()

    def window_handle(self):
        '''
        Returns the handle of the current window.
        Usage:
            driver.windows_handle
        '''
        return self.driver.current_window_handle

    def window_handles(self):
        '''
        Returns the a all handle of the current window.
        Usage:
            driver.windows_handles
        '''
        return self.driver.window_handles

    def switch_to_window(self, handle):
        '''
        Switch to the specified window.
        Usage:
        driver.switch_to_window(handle)
        '''
        self.driver._switch_to.window(handle)

    def open_new_window(self, css):
        '''
        Open the new window and switch the handle to the newly opened window.
        Usage:
        driver.open_new_window()
        '''
        original_windows = self.driver.current_window_handle
        el = self.get_element(css)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver._switch_to.window(handle)


    def is_element_exist(self,css):
        '''
        先检验元素是否存在，若存在则利用js把div删除，方便定位后面的元素。
        若没有这个元素，则可以直接运行后面的元素。
        '''
        try:
            e = self.get_element(css)
            self.js("var rm=document.getElementById('roomform').removeChild(document.getElementById('roomform').children[5])")
            self.js("var rm=document.getElementById('describeform').removeChild(document.getElementById('describeform').children[15])")

        except:
            m = print("没有此div")
            return m



