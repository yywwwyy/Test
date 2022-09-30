# encoding=utf-8
"""
@Description :
@Project ：behavior-recognition
@File    ：recognition_methods.py
@Author  ：
@Date    ：
"""

import json
import time
import datetime
from recognition_base import Recognition


class Other_recognition(Recognition):
    def __init__(self, data):
        super().__init__(data=data)

    def data_deal(self):
        """
            行为结构化（出门、卫生间等）数据处理，输出格式为 list
        :return:
        """

        user_data = self.data

        # try:
        # 待补充
        # except:
        # 待补充

        '''
        # 此处为按时间整理数据
        data_org = list(zip(user_data['place'], user_data['timestamp'])) # zip 使place与timestamp以pair的形式排列
        data_org_sort = sorted(data_org, key=lambda x: x[1]) # 以时间顺序排序
        data_org_sort = list(zip(*data_org_sort)) # 一个包含两个tuple的list
        place_list=list(data_org_sort[0])
        timestamp_list=list(data_org_sort[1])
        '''
        # 等待需求
        # return place_list, timestamp_list

    def tolit_recogn(self):
        """
            处理出卫生间活动的信息，输出格式为 int, float, list
        :return:
        """
        tolit_times = 0
        tolit_total_time = 0.0
        tolit_mean_time = tolit_total_time / tolit_times
        tolit_time_start = []
        tolit_time_stop = []
        tolit_time_range = []

        '''
        算法待加入
        '''

        return tolit_times, tolit_total_time, tolit_mean_time, \
               tolit_time_start, tolit_time_stop, tolit_time_range

    def outside_recogn(self):
        """
            处理出外出活动的信息，输出格式为 int, float, list
        :return:
        """
        outside_times = 0
        outside_total_time = 0.0
        outside_mean_time = outside_total_time / outside_times
        outside_time_start = []
        outside_time_stop = []
        outside_time_range = []

        '''
        算法待加入
        '''

        return outside_times, outside_total_time, outside_mean_time, \
               outside_time_start, outside_time_stop, outside_time_range


class Sleep_recognition(Recognition):
    def __init__(self, data):
        super().__init__(data=data)

    def data_deal(self):
        """
            行为结构化——睡眠数据处理，输出格式为 list
        :return:
        """

        user_data = self.data

        # try:
        # 待补充
        # except:
        # 待补充

        # 等待需求
        # return

    def sleep_recogn(self):
        """
            睡眠活动的识别，输出格式为
        :return:
        """

        # 等待需求
        # return


