# encoding=utf-8
"""
@Description :
@Project ：behavior-recognition
@File    ：main.py
@Author  ：
@Date    ：
"""

from flask import Flask, request
import json
from recognition_methods import *
from util import load_config
# import logging

app = Flask(__name__)
conf_dic = load_config()


# 行为结构化（出门、卫生间等）
@app.route('/behavior-recognition/others', methods=['POST'])
def recognition_other():
    """
        :Author:
        :Create:
    """
    """
    :return: result
    """
    # result 为最终返回
    result = dict()
    result['status'] = 200
    result['errno'] = 200

    # 请求数据为json,我们使用request.data来获取
    user_data = request.data.decode('utf-8')

    try:
        user_data = json.loads(user_data, encoding='utf-8')
    except Exception as e:
        result['status'] = 200
        result['errno'] = 3003
        result['msg'] = '数据格式错误' + str(e)
        result = json.dumps(result, ensure_ascii=False)
        return result

    recognition_other_usr = Other_recognition(user_data)

    tolit_recogn_result = dict()
    tolit_recogn_result["tolit_times"], tolit_recogn_result["tolit_total_time"], tolit_recogn_result["tolit_mean_time"], \
    tolit_recogn_result["tolit_time_start"], tolit_recogn_result["tolit_time_stop"], \
    tolit_recogn_result["tolit_time_range"] = recognition_other_usr.tolit_recogn()

    outside_recogn_result = dict()
    outside_recogn_result["tolit_times"], outside_recogn_result["tolit_total_time"], outside_recogn_result["tolit_mean_time"], \
    outside_recogn_result["tolit_time_start"], outside_recogn_result["tolit_time_stop"], \
    outside_recogn_result["tolit_time_range"] = recognition_other_usr.outside_recogn()

    result_msg_dict = dict()
    result_msg_dict['tolit'] = tolit_recogn_result
    result_msg_dict['outside'] = outside_recogn_result
    result['msg'] = result_msg_dict

    # logger.debug('返回结果：%s' % result)
    result = json.dumps(result, ensure_ascii=False)
    return result


# 行为结构化——睡眠识别
@app.route('/behavior-recognition/sleep', methods=['POST'])
def recognition_sleep():
    """
        :Author:
        :Create:
    """
    """
    :return: result
    """
    result = dict()
    result['status'] = 200
    result['errno'] = 200

    user_data = request.data.decode('utf-8')

    try:
        user_data = json.loads(user_data, encoding='utf-8')
    except Exception as e:
        result['status'] = 200
        result['errno'] = 3003
        result['msg'] = '数据格式错误' + str(e)
        result = json.dumps(result, ensure_ascii=False)
        return result

    # 待补充

    return result


if __name__ == '__main__':
    app.run(host=conf_dic['host'], port=conf_dic['port'], debug=True)
