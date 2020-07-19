#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_allure_attach.py
@time: 2020/07/15
@remark：attach用于在测试报告中添加附件，附件可以为网页或图片
attachment_type:
    TEXT = ("text/plain", "txt")
    CSV = ("text/csv", "csv")
    TSV = ("text/tab-separated-values", "tsv")
    URI_LIST = ("text/uri-list", "uri")

    HTML = ("text/html", "html")
    XML = ("application/xml", "xml")
    JSON = ("application/json", "json")
    YAML = ("application/yaml", "yaml")
    PCAP = ("application/vnd.tcpdump.pcap", "pcap")

    PNG = ("image/png", "png")
    JPG = ("image/jpg", "jpg")
    SVG = ("image/svg-xml", "svg")
    GIF = ("image/gif", "gif")
    BMP = ("image/bmp", "bmp")
    TIFF = ("image/tiff", "tiff")

    MP4 = ("video/mp4", "mp4")
    OGG = ("video/ogg", "ogg")
    WEBM = ("video/webm", "webm")

    PDF = ("application/pdf", "pdf")
"""
import allure


# 在allure中显示纯文本信息
def test_attach_text():
    allure.attach("这是纯文本信息", attachment_type=allure.attachment_type.TEXT)


# 在allure中显示html
def test_attach_html():
    allure.attach("<body>这是一段html</body>", name="html测试", attachment_type=allure.attachment_type.HTML)


# 在allure中显示图片
def test_attach_image():
    allure.attach.file("/Users/doulihang/work/project/weeds_study/pytest_study/resouces/image.jpg",
                       name="帅帅的图片",
                       attachment_type=allure.attachment_type.JPG
                       )
