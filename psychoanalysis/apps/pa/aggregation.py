from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from itertools import chain


def make_query(query_dict):
    query_type = 0
    if 'result type' in query_dict:
        if query_dict['result type'] == 'percent':
            query_type = 1

    data_set = 0
    if 'data set' in query_dict:
        data_set = 2

    the_list = get_data_set(data_set)

    return the_list


def get_data_set(num=0):
    if num == 0:
        return get_data_set_0()
    if num == 1:
        return get_data_set_1()
    if num == 2:
        return get_data_set_2()
    return get_data_set_3()


def get_data_set_0():
    data_list = []
    data_list.append(['Activity', 'Consultant Clinical Psychologist', 'Clinical Psychologist 1', 'Clinical Psychologist 2', 'Clinical Psychologist 3', 'CAAP', 'CAAP Trainee', 'Clinical Psychology Trainee'])
    data_list.append(['Assessment', 60,  120,  0,  240,  0,  0,  120])
    data_list.append(['Individual Follow up', 990,  1140,  180,  120,  315,  495,  330])
    data_list.append(['Low Intensity', 0,  0,  0,  0,  0,  60,  0])
    data_list.append(['High Intensity', 60,  0,  0,  0,  315,  435,  0])
    data_list.append(['High Intensity - Specialist', 375,  660,  0,  0,  0,  0,  330])
    data_list.append(['Highly Specialist', 555,  480,  180,  240,  0,  0,  0])
    data_list.append(['Group Therapy', 0,  0,  270,  285,  90,  0,  0])
    data_list.append(['Case review (with patient)', 0,  0,  0,  0,  0,  0,  0])
    data_list.append(['Other Treatment', 0,  0,  0,  0,  30,  0,  0])
    data_list.append(['Clinical Administration', 750,  1230,  315,  660,  645,  990,  465])
    data_list.append(['Telephone', 0,  30,  30,  0,  0,  0,  105])
    data_list.append(['Clinical meeting', 195,  300,  0,  60,  75,  90,  15])
    data_list.append(['Supervision - giving', 60,  360,  0,  120,  75,  0,  60])
    data_list.append(['Supervision - receiving', 0,  90,  0,  0,  180,  60,  60])
    data_list.append(['Other Supervision', 0,  0,  0,  0,  0,  0,  0])
    data_list.append(['Admin tasks', 165,  255,  15,  75,  0,  225,  75])
    data_list.append(['Dealing with emails', 525,  420,  0,  60,  90,  75,  105])
    data_list.append(['Travel', 270,  525,  75,  180,  210,  120,  135])
    data_list.append(['Meetings (non-clinical)', 1050,  330,  30,  135,  0,  0,  0])
    data_list.append(['Research', 30,  75,  0,  45,  30,  0,  0])
    data_list.append(['Training/ CPD (Delivering)', 0,  0,  0,  0,  0,  0,  0])
    data_list.append(['Training/ CPD (Receiving)', 0,  15,  0,  0,  0,  450,  0])
    data_list.append(['Annual Leave', 0,  0,  0,  0,  480,  540,  0])
    data_list.append(['Sick Leave', 0,  0,  0,  0,  0,  0,  0])
    data_list.append(['Other leave', 0,  0,  0,  0,  240,  0,  540])
    data_list.append(['Breaks', 195,  15,  45,  90,  45,  150,  90])
    data_list.append(['Management', 735,  15,  0,  0,  30,  30,  0])
    data_list.append(['Other Management', 0,  345,  0,  0,  0,  0,  30])
    return data_list


def get_data_set_1():
    the_list = get_data_set_0()
    percent_list = ['Time Recorded', 5025,  5265,  960,  2070,  2535,  3225,  2130]

    num = 0
    ret_list = []
    for item in the_list:
        if num == 0:
            ret_list.append(item)
        else:
            ret_list.append(percent_item(item, percent_list))
        num += 1

    return ret_list


def get_data_set_2():
    main_list = get_category_data_set()
    data_list = []
    data_list.append(['Category', 'Consultant Clinical Psychologist', 'Clinical Psychologist 1', 'Clinical Psychologist 2', 'Clinical Psychologist 3', 'CAAP', 'CAAP Trainee', 'Clinical Psychology Trainee'])
    direct_list = get_one_catergory_data('Direct', main_list)
    indirect_list = get_one_catergory_data('Indirect', main_list)
    other_list = get_one_catergory_data('Other', main_list)
    data_list.append(direct_list)
    data_list.append(indirect_list)
    data_list.append(other_list)

    return data_list


def get_data_set_3():
    the_list = get_data_set_2()
    percent_list = ['Time Recorded', 5025,  5265,  960,  2070,  2535,  3225,  2130]

    num = 0
    ret_list = []
    for item in the_list:
        if num == 0:
            ret_list.append(item)
        else:
            ret_list.append(percent_item(item, percent_list))
        num += 1

    return ret_list


def get_category_data_set():
    data_list = []
    data_list.append(['Direct', 60, 120, 0, 240, 0, 0, 120])
    data_list.append(['Direct', 990, 1140, 180, 120, 315, 495, 330])
    data_list.append(['Direct', 0, 0, 0, 0, 0, 60, 0])
    data_list.append(['Direct', 60, 0, 0, 0, 315, 435, 0])
    data_list.append(['Direct', 375, 660, 0, 0, 0, 0, 330])
    data_list.append(['Direct', 555, 480, 180, 240, 0, 0, 0])
    data_list.append(['Direct', 0, 0, 270, 285, 90, 0, 0])
    data_list.append(['Direct', 0, 0, 0, 0, 0, 0, 0])
    data_list.append(['Direct', 0, 0, 0, 0, 30, 0, 0])
    data_list.append(['Indirect', 750, 1230, 315, 660, 645, 990, 465])
    data_list.append(['Indirect', 0, 30, 30, 0, 0, 0, 105])
    data_list.append(['Indirect', 195, 300, 0, 60, 75, 90, 15])
    data_list.append(['Indirect', 60, 360, 0, 120, 75, 0, 60])
    data_list.append(['Indirect', 0, 90, 0, 0, 180, 60, 60])
    data_list.append(['Indirect', 0, 0, 0, 0, 0, 0, 0])
    data_list.append(['Other', 165, 255, 15, 75, 0, 225, 75])
    data_list.append(['Other', 525, 420, 0, 60, 90, 75, 105])
    data_list.append(['Other', 270, 525, 75, 180, 210, 120, 135])
    data_list.append(['Other', 1050, 330, 30, 135, 0, 0, 0])
    data_list.append(['Other', 30, 75, 0, 45, 30, 0, 0])
    data_list.append(['Other', 0, 0, 0, 0, 0, 0, 0])
    data_list.append(['Other', 0, 15, 0, 0, 0, 450, 0])
    data_list.append(['Other', 0, 0, 0, 0, 480, 540, 0])
    data_list.append(['Other', 0, 0, 0, 0, 0, 0, 0])
    data_list.append(['Other', 0, 0, 0, 0, 240, 0, 540])
    data_list.append(['Other', 195, 15, 45, 90, 45, 150, 90])
    data_list.append(['Other', 735, 15, 0, 0, 30, 30, 0])
    data_list.append(['Other', 0, 345, 0, 0, 0, 0, 30])
    return data_list


def get_one_catergory_data(category, data_list):
    the_len = len(data_list[0])
    ret_list = []
    ret_list.append(category)
    for num in range(1, the_len):
        ret_list.append(0)

    for sub_list in data_list:
        if sub_list[0] != category:
            continue

        for index in range(1, the_len):
            tot = sub_list[index] + ret_list[index]
            ret_list[index] = tot

    return ret_list


def percent_item(item, percent_list):
    num = 0
    ret_list = []
    for val in item:
        if num == 0:
            ret_list.append(val)
        else:
            result = val * 100.0 / percent_list[num]
            ret_list.append(result)
        num += 1
    return ret_list
