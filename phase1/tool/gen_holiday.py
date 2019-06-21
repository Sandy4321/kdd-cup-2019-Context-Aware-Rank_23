# coding=gbk
import pandas as pd

server_url = "http://api.goseek.cn/Tools/holiday?date="
import urllib.request
import json
import datetime
def crawel_holiday():
    '''
    �����Ѿ���20170101  �� 20181220 ���������ڱ�ʶ��Ϣ
    �������������ն�Ӧ���Ϊ 0, �����ڼ��ն�Ӧ���Ϊ 1, �ڼ��յ��ݲ����Ӧ�Ľ��Ϊ 2����Ϣ�ն�Ӧ���Ϊ 3
    '''
    start_data='2018-06-01 19:00:00'
    end_data = '2018-12-20 19:00:00'
    start_timestamp = pd.to_datetime(start_data)
    end_timestamp = pd.to_datetime(end_data)
    have_holiday=pd.read_csv('../data/holiday_bj.csv')
    have_holiday.pop('lunardate') #��Ҫũ��
    print('----    ��ʼѭ����������    ----')
    while start_timestamp<=end_timestamp:
        i=str(start_timestamp)
        resp = urllib.request.urlopen(server_url + str(i[0:4]) + str(i[5:7]) + str(i[8:10]))
        html = json.loads(resp.read())
        date_flag = html['data']
        print('the date_flag:',date_flag)

        new = pd.DataFrame({"date": str(i[0:4]) + str(i[5:7]) + str(i[8:10]),  "holiday": date_flag}, index=["0"])
        have_holiday =have_holiday.append(new,ignore_index=True)
        have_holiday.to_csv('../data/holiday_china_all.csv')
        start_timestamp = start_timestamp + datetime.timedelta(hours=24)

crawel_holiday()