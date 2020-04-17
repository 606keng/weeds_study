#!/usr/bin/env python
#-*-coding: UTF-8 -*-
'''


'''


import os
def check_devices(adb,udid):
    error = 'This is not found devices：%s ,Check if the Android phone is connected properly！！！'%(udid)
    if os.name == "posix":
        result = os.system("%s devices|grep %s" % (adb, str(udid)))
    elif os.name == "nt":
        result = os.system("%s devices|findStr %s " % (adb, str(udid)))
    if result != 0:
        raise RuntimeError(error)





def caps(func):
    def _caps(self,udid,app_path,adb_path="adb",aapt_path="aapt",isApp=False,isResetKeyboard=False):
        #check adb 、aapt
        check_devices(adb_path,udid)
        if os.name == "posix":
            aapt_dump = "%s dump badging %s |grep %s|awk '{print $2}'"
            appPackage = str(os.popen(aapt_dump % (aapt_path, app_path, "package")).read()).strip()[6:-1]
            # print(aapt_dump % (aapt_path,app_path, "launchable-activity"))
            try:
                appActivity = str(
                    os.popen(aapt_dump % (aapt_path,app_path, "launchable-activity")).read()).split()[0].strip()[6:-1]
            except Exception as e:
                appActivity = appPackage+".main.MainActivity"

        elif os.name == "nt":
            appPackage = os.popen('aapt dump badging  %s |findStr "package:" ' % (app_path)).read().split(" ")[1].strip()[6:-1]
            try:
                appActivity = os.popen('aapt dump badging %s |findStr "launchable-activity"' % (app_path)).read().split(" ")[1].strip()[
            6:-1]
            except:
                appActivity = appPackage + ".main.MainActivity"

            # udids = str(os.popen("%s devices|grep -v devices|awk '{print $1}'" % (self.adb_path)).read()).split("\n")
            # udids = list(filter(None, udids))
        android_version = os.popen("%s -s %s shell getprop ro.build.version.release" % (adb_path,udid)).read().strip()
        android_name = os.popen("%s -s %s shell getprop ro.product.name" % (adb_path,udid)).read().strip()
        if int(android_version[0]) <= 4:
            error = "Android Version must be greater than 4 !"
            raise RuntimeError(error)

        caps = {"platformName": "android",
                "platformVersion": android_version,
                "app": app_path,
                "udid": udid,
                # "newCommandTimeout":100000,
                "deviceName": android_name,
                "appPackage": appPackage,
                "appActivity": appActivity}
        if isResetKeyboard == True:
            caps.update({'unicodeKeyboard': True,
                         'resetKeyboard': True})
        if isApp == True:
            caps.update({"noReset": True})

        return func(self,udid, caps)
    return _caps



def isAppium(func):
    def _isAppium(self):
        random_port = func(self)
        # time.sleep(8)
        if os.name == "posix":
            pid = os.popen("lsof -i:%s|grep node|awk '{print $2}'"%str(random_port)).read()
        elif os.name == "nt":
            pid  = os.popen("netstat -ano|findStr %s"%str(random_port)).read()[-8:].strip()
        func(self)
        if len(pid) != 0:
            return True
        return False
    return _isAppium



def closeServer(func):
    def _closeServer(self):
       random_port = func(self)
       if os.name == "posix":
            pid = os.popen("lsof -i:%s|grep node|awk '{print $2}'" % str(random_port)).read()
            return os.system("kill " + pid)
       elif os.name == "nt":
           netPort = os.popen("netstat -ano|findStr 1125").read()[-8:].strip()
           return os.system("taskkill /pid %s -t -f"%netPort)
    return _closeServer

def get_element(func):
    def _get_element(self,typed,element):
        driver = func(self)
        if "id" in typed:
            if "id" == typed:
                return driver.find_element_by_id(element)
            else:
                return driver.find_elements_by_id(element)
        elif "xpath" in typed:
            if "xpath" == typed:
                return driver.find_element_by_xpath(element)
            else:
                return driver.find_elements_by_xpath(element)

        elif "class" in typed:
            if "class" == typed:
                return driver.find_element_by_class_name(element)
            else:
                return driver.find_elements_by_class_name(element)

        elif "link_text" in typed:
            if "link_text" == typed:
                return driver.find_element_by_link_text(element)

            else:
                return driver.find_elements_by_link_text(element)

        elif "partial_link_text" in typed:
            if "partial_link_text" == typed:
                return driver.find_element_by_partial_link_text(element)

            else:
                return driver.find_elements_by_partial_link_text(element)

        elif "tag_name" in typed:
            if "tag_name" == typed:
                return driver.find_element_by_tag_name(element)

            else:
                return driver.find_elements_by_tag_name(element)

        elif "name" in typed:
            if "name" == typed:
                return driver.find_element_by_name(element)

            else:
                return driver.find_elements_by_name(element)

        elif "css_selector" in typed:
            if "css_selector" == typed:
                return driver.find_element_by_css_selector(element)

            else:
                return driver.find_elements_by_css_selector(element)
        raise RuntimeError("The location element was not found, please check whether the element is correct!!!")
    return _get_element