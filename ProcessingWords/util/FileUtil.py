#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 14:53
# @Author  : suojijun1994@gmail.com
# @Site    :
# @File    : Reply.py
# @Software: PyCharm
import os
import json
from timeUtils import current_time
from DataStructure.Article import Article
from DataStructure.Comment import Comment
from DataStructure.Reply import Reply

class PathHelper(object):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')
    RESULTS_DIR = os.path.join(BASE_DIR, 'results')

    @classmethod
    def generate_result_id(self):
        filename = "result_" + current_time() + ".json"
        filepath = os.path.join(self.RESULTS_DIR, str(filename))
        return filepath

    @classmethod
    def get_resource_abs_path(self, filename):
        filepath = os.path.join(self.RESOURCES_DIR, str(filename))
        return filepath

    @classmethod
    def get_result_abs_path(self, filename):
        filepath = os.path.join(self.RESULTS_DIR, str(filename))
        return filepath

    @classmethod
    def json2obj(self, jdata):
        article_obj = Article()
        article_obj.__dict__.update(jdata)
        # comments字典数组转换为对象数组
        comms = []
        for comm_dict in article_obj.comments:
            commment_obj = Comment()
            commment_obj.__dict__.update(comm_dict)
            comms.append(commment_obj)
            # reply字典数组转换为对象数组
            replies = []
            for reply_dict in commment_obj.replies:
                reply_obj = Reply()
                reply_obj.__dict__.update(reply_dict)
                replies.append(reply_obj)
            commment_obj.replies = replies
        article_obj.comments = comms
        return article_obj

    @classmethod
    def get_array_from_json(self, filename):
        filepath = self.get_result_abs_path(filename)
        blogs = []
        with open(filepath, 'r') as f:
            while True:
                line = f.readline().decode('UTF-8')
                if not line:
                    break
                jline = json.loads(line, encoding="UTF-8")
                obj = self.json2obj(jline)
                blogs.append(obj)
        return blogs

# just for testing
if __name__ == '__main__':
    # print(PathHelper.BASE_DIR)
    # print(PathHelper.RESOURCES_DIR)
    # print(PathHelper.RESULTS_DIR)
    #
    # print(PathHelper.generate_result_id())
    # print(PathHelper.get_resource_abs_path("test.xlsx"))

    jf = PathHelper.get_array_from_json('result_20181220_203935.json')
