#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: driver_util.py.py
@time: 2020/12/14 
"""
import json
import os
import zipfile
import shutil
import requests
import pathlib
from win32com import client as win_client


# 工作目录（当前路径调试时需加上.parent）
BASE_DIR = str(pathlib.Path.cwd())
# BASE_DIR = str(pathlib.Path.cwd().parent)

CHROME_DRIVER_BASE_URL = "https://chromedriver.storage.googleapis.com"
EDGE_DRIVER_BASE_URL = "https://msedgedriver.azureedge.net"
CHROME_DRIVER_ZIP = "chromedriver_win32.zip"
EDGE_DRIVER_ZIP = "edgedriver_win64.zip"
CHROME_DRIVER = "chromedriver.exe"
EDGE_DRIVER = "msedgedriver.exe"

BROWSER_DRIVER_DIR = str(pathlib.PurePath(BASE_DIR, "driver"))
DRIVER_MAPPING_FILE = os.path.join(BASE_DIR, "config", "mapping.json")

def get_browser_version(file_path):
    """
    获取浏览器版本
    :param file_path: 浏览器文件路径
    :return: 浏览器大版本号
    """
    # 判断路径文件是否存在
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} is not found.")
    win_obj = win_client.Dispatch('Scripting.FileSystemObject')
    version = win_obj.GetFileVersion(file_path)

    return version.strip()


def get_browser_major_version(file_path):
    """
    获取浏览器大版本号
    :param file_path: 浏览器文件路径
    :return: 浏览器大版本号
    """
    browser_ver = get_browser_version(file_path)
    browser_major_ver = browser_ver.split(".")[0]

    return browser_major_ver


def get_latest_browser_version(browser_major_ver):
    """
    获取匹配大版本的最新release版本
    :param browser_major_ver: 浏览器大版本号
    :return: 最新release版本号
    """
    latest_api = f"{CHROME_DRIVER_BASE_URL}/LATEST_RELEASE_{browser_major_ver}"
    resp = requests.get(latest_api)
    latest_driver_version = resp.text.strip()

    return latest_driver_version
def download_browser_driver(latest_driver_version, browser_name):
    """
    下载浏览器驱动压缩包
    :param browser_name: 浏览器名称
    :param latest_driver_version: 浏览器的版本号
    """
    download_api = None
    if browser_name == "Chrome":
        download_api = f"{CHROME_DRIVER_BASE_URL}/{latest_driver_version}/{CHROME_DRIVER_ZIP}"
    elif browser_name == "Edge":
        download_api = f"{EDGE_DRIVER_BASE_URL}/{latest_driver_version}/{EDGE_DRIVER_ZIP}"

    download_dir = os.path.join(str(BROWSER_DRIVER_DIR), os.path.basename(download_api))
    # 下载，设置超时时间20s
    resp = requests.get(download_api, stream=True, timeout=20)

    if resp.status_code == 200:
        with open(download_dir, 'wb') as fo:
            fo.write(resp.content)
    else:
        raise Exception("Download chrome driver failed")
def unzip_driver(browser_major_ver, browser_name):
    """
    解压驱动压缩包
    :param browser_name: 浏览器名称
    :param browser_major_ver: 浏览器大版本号
    :return: 驱动文件路径
    """
    file_path = None
    driver_path = None

    if browser_name == "Chrome":
        file_path = os.path.join(BROWSER_DRIVER_DIR, os.path.basename(CHROME_DRIVER_ZIP))
        driver_path = os.path.join(BROWSER_DRIVER_DIR, browser_major_ver, CHROME_DRIVER)
    elif browser_name == "Edge":
        file_path = os.path.join(BROWSER_DRIVER_DIR, os.path.basename(EDGE_DRIVER_ZIP))
        driver_path = os.path.join(BROWSER_DRIVER_DIR, browser_major_ver, EDGE_DRIVER)
    browser_driver_dir = os.path.join(BROWSER_DRIVER_DIR, browser_major_ver)

    # 解压到指定目录
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(browser_driver_dir)

    return driver_path


def remove_driver_zip(browser_name):
    """
    删除下载的驱动压缩包
    :param browser_name: 浏览器名称
    """
    file_path = None
    if browser_name == "Chrome":
        file_path = os.path.join(BROWSER_DRIVER_DIR, os.path.basename(CHROME_DRIVER_ZIP))
    elif browser_name == "Edge":
        file_path = os.path.join(BROWSER_DRIVER_DIR, os.path.basename(EDGE_DRIVER_ZIP))
    os.remove(file_path)
def read_driver_mapping_json():
    """
    读取 mapping_json
    :return: 字典格式
    """
    if os.path.exists(DRIVER_MAPPING_FILE):
        with open(DRIVER_MAPPING_FILE) as fo:
            try:
                driver_mapping_dict = json.load(fo)
            # mapping.json内容为空时，返回空字典
            except json.decoder.JSONDecodeError:
                driver_mapping_dict = {}
    else:
        raise FileNotFoundError(f"{DRIVER_MAPPING_FILE} is not found")

    return driver_mapping_dict


def write_driver_mapping_json(browser_major_ver, latest_driver_version, driver_path, browser_name):
    """
    写入 mapping_json
    :param browser_major_ver: 浏览器大版本号
    :param latest_driver_version: 浏览器驱动版本号
    :param driver_path: 驱动存放路径
    :param browser_name: 浏览器名称
    """
    mapping_dict = read_driver_mapping_json()
    # 版本号在dict中（浏览器名不在dict中）
    if browser_major_ver in mapping_dict:

        mapping_dict[browser_major_ver][browser_name] = {
                            "driver_path": driver_path,
                            "driver_version": latest_driver_version
                }
    # 大版本号不在dict中，且字典不为空
    elif browser_major_ver not in mapping_dict and mapping_dict:
        mapping_dict[browser_major_ver] = {
            browser_name:
                {
                    "driver_path": driver_path,
                    "driver_version": latest_driver_version
                }
        }
    # 字典为空
    else:
        mapping_dict = {
            browser_major_ver:
                {
                    browser_name:
                        {
                            "driver_path": driver_path,
                            "driver_version": latest_driver_version
                        }
                }
        }
        mapping_dict.update(mapping_dict)

    with open(DRIVER_MAPPING_FILE, 'w') as fo:
        json.dump(mapping_dict, fo)
def automatic_discover_driver(browser_path, browser_name="Chrome"):
    """
    侦测浏览器驱动是否在mapping.json有记录，否则下载该驱动
    :param browser_path: 浏览器路径
    :param browser_name: 浏览器名称
    """
    browser_maj_ver = get_browser_major_version(browser_path)
    # Chrome需要获取大版本号对应的latest release version
    # Edge 可直接用当前浏览器版本号
    if browser_name == "Chrome":
        latest_browser_ver = get_latest_browser_version(browser_maj_ver)
    elif browser_name == "Edge":
        latest_browser_ver = get_browser_version(browser_path)
    else:
        raise Exception(f"{browser_name} is not found")

    # 读取mapping.json内容
    mapping_dict = read_driver_mapping_json()

    # json为空 或版本号不在mapping_dict中 或浏览器名不在mapping_dict中
    if not mapping_dict or \
            browser_maj_ver not in mapping_dict or \
            browser_name not in mapping_dict[browser_maj_ver]:

        # 下载浏览器驱动压缩包
        download_browser_driver(latest_browser_ver, browser_name)
        # 解压浏览器驱动压缩包，并返回驱动路径
        driver_path = unzip_driver(browser_maj_ver, browser_name)
        # 将浏览器大版本号、浏览器名、驱动路径、对应的浏览器版本号信息写入到mapping.json中
        write_driver_mapping_json(browser_maj_ver, latest_browser_ver, driver_path, browser_name)

        # 删除浏览器驱动压缩包
        remove_driver_zip(browser_name)

    # 返回浏览器驱动的路径
    mapping_dict = read_driver_mapping_json()
    return mapping_dict[browser_maj_ver][browser_name]["driver_path"]
