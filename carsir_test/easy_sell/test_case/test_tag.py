#!usr/bin/env python
#-*- coding:utf-8 -*-
import json

import pytest
from jsonpath import jsonpath

from request_study.api_ddatf.api.tag import Tag


class TestTag:
    @classmethod
    def setup_class(cls):
        cls.tag = Tag()
    @pytest.mark.parametrize("name_old, name_new",[
        ("wangwu","haha"),
        ("zhangsan","dou")
    ])
    def test_all(self):
        """
        1.添加名称为豆豆的tag
        2.查看是否有名称为豆豆的tag
        3.将豆豆更新为野草
        4.删除名称为野草的tag
        :return:
        """
        # 添加名称为豆豆的tag
        self.tag.add(tag_name="豆豆")
        #查看是否有名称为豆豆的tag
        print(jsonpath(self.tag.get(), "$..name"))
        #更新tag名称为野草
        tag_id = self.tag.jsonpath(self.tag.get(),"$..tag[?(@.name=='豆豆')].id")[0]
        # tag_id = jsonpath(self.tag.get(), "$..tag[?(@.name=='豆豆')].id")[0]
        self.tag.update(tag_id=tag_id,tag_name="野草")
        print(jsonpath(self.tag.get(), "$..name"))
        #删除名称为野草的tag
        self.tag.delete(tag_id=tag_id)
        # if tag_id:
        #     self.tag.delete(tag_id[0])
        # self.tag.add("wangwu")
        # tag_id = jsonpath(self.tag.get(), "$..tag[?(@.name=='wangwu')].id")
        # self.tag.update(tag_id=tag_id[0],tag_name="gaogao")

    def test_add(self):
        print(self.tag.add(tag_name="zhangsan"))

    def test_get(self):
        #以json格式输出
        print(json.dumps(self.tag.get(),indent=2,ensure_ascii=False))

    def test_delete(self):
        print(self.tag.delete(tag_id="et3h9GCwAAiKjjUFhjN25BzW6lao-gEQ"))

    def test_update(self):
        print(self.tag.update(tag_id="et3h9GCwAAhzPFzB6WIZOzJUKLdfb7BQ", tag_name="doudou"))
