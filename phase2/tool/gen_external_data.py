# coding=gbk
'''

    ��ȡ�ĵ�ַ��http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi
    ��ȡ�õ�keyֵΪ��LlNVsWOsqmKwlqkUEBmzbpmbu2GAc2Dl
    http://api.map.baidu.com/place/v2/search?query=ATM��&tag=����&region=����&output=json&ak=LlNVsWOsqmKwlqkUEBmzbpmbu2GAc2Dl
'''

import pandas as pd
import urllib.request
import json
import re
import time


http='http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location=35.658651,139.745415&output=json&pois=1&latest_admin=1&ak=hCedZFZlgn8lOvvOId5hrXdvDZVQDrKr'

# def gen_all_address():
#     data=pd.read_csv('../data_set_phase1/feature_data/feature.csv')
#     # the_orig_lng=data['o_lng']
#     # the_orig_lat=data['o_lat']
#     # the_des_lng=data['d_lng']
#     # the_des_lat=data['d_lat']
#     print(2)
#     the_quyu=[]
#     print(len(data.index))
#     for indexs in data.index:
#         print(len(the_quyu))
#         resp_orig = urllib.request.urlopen('http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location='+str(data.loc[indexs]['o_lat'])+','+str(data.loc[indexs]['o_lng'])+'&output=json&pois=1&latest_admin=1&ak=hCedZFZlgn8lOvvOId5hrXdvDZVQDrKr')
#         resp_str=str(resp_orig.read().decode('utf8'))
#         resp_str=resp_str[29:-2]
#
#
#         p1 = r"������.*��"
#         pattern1 = re.compile(p1)
#
#         the_quyu.append(pattern1.findall(resp_str)[0].split('������')[1].split('��')[0])
#
#         time.sleep(1)
#         #############   ʹ��������ʽ���н�����ȡ   ##############
#     print(the_quyu)
#
#     return the_quyu
#
# def test_zhengze():
#     my_txt='{"status":0,"result":{"location":{"lng":116.28999999999994,"lat":39.97000007254172},"formatted_address":"�����к��������峧��·","business":"���ͳ�,�ļ���,Զ��·","addressComponent":{"country":"�й�","country_code":0,"country_code_iso":"CHN","country_code_iso2":"CN","province":"������","city":"������","city_level":2,"district":"������","town":"","adcode":"110108","street":"���峧��·","street_number":"","direction":"","distance":""},"pois":[{"addr":"�����к��������峧��ס�����ͳ�3�ڴ���԰6��¥","cp":" ","direction":"��","distance":"102","name":"�й���������(����Զ����·֧��)","poiType":"����","point":{"x":116.28983435050277,"y":39.96930388943203},"tag":"����;����","tel":"","uid":"d4034eb38a6c2ff6c0364441","zip":"","parent_poi":{"name":"","tag":"","addr":"","point":{"x":0.0,"y":0.0},"direction":"","distance":"","uid":""}},{"addr":"���峧��·19��","cp":" ","direction":"����","distance":"203","name":"���峧������","poiType":"���ξ���","point":{"x":116.29121774098813,"y":39.971045708291629},"tag":"���ξ���;����","tel":"","uid":"5191bb9a6696551b1ce99987","zip":"","parent_poi":{"name":"","tag":"","addr":"","point":{"x":0.0,"y":0.0},"direction":"","distance":"","uid":""}},{"addr":"�����к��������峧����԰С��5��¥","cp":" ","direction":"����","distance":"233","name":"���峧����԰","poiType":"���ز�","point":{"x":116.2883162141909,"y":39.969034318229848},"tag":"���ز�;סլ��","tel":"","uid":"34f68ab038f0530a8e55ecac","zip":"","parent_poi":{"name":"","tag":"","addr":"","point":{"x":0.0,"y":0.0},"direction":"","distance":"","uid":""}},{"addr":"�����к��������峧���԰С��9��¥","cp":" ","direction":"����","distance":"250","name":"���峧���԰","poiType":"���ز�","point":{"x":116.29195435150632,"y":39.96913799958826},"tag":"���ز�;סլ��","tel":"","uid":"e93761f6bb9d9572223bf270","zip":"","parent_poi":{"name":"","tag":"","addr":"","point":{"x":0.0,"y":0.0},"direction":"","distance":"","uid":""}},{"addr":"����·�����峧��·���������150��","cp":" ","direction":"����","distance":"161","name":"���ֵ���ܰ��԰","poiType":"���ز�","point":{"x":116.28907977387439,"y":39.970859086982319},"tag":"���ز�;סլ��","tel":"","uid":"7bcfc17f6fa9933e077ce8aa","zip":"","parent_poi":{"name":"","tag":"","addr":"","point":{"x":0.0,"y":0.0},"direction":"","distance":"","uid":""}},{"addr":"�����������ű�300��","cp":" ","direction":"��","distance":"216","name":"���ͳ�(����)","poiType":"���ز�","point":{"x":116.29049909658015,"y":39.97144659677496},"tag":"���ز�;סլ��","tel":"","uid":"75fa23f1956124bed3ff23bb","zip":"","parent_poi":{"name":"","tag":"","addr":"","point":{"x":0.0,"y":0.0},"direction":"","distance":"","uid":""}},{"addr":"���������峧��·����԰��4��¥","cp":" ","direction":"��","distance":"378","name":"�й���������(�������ͽ�Դ֧��)","poiType":"����","point":{"x":116.29070570684745,"y":39.96743760529318},"tag":"����;����","tel":"","uid":"861a8cf81cd8b28dfb2d6117","zip":"","parent_poi":{"name":"","tag":"","addr":"","point":{"x":0.0,"y":0.0},"direction":"","distance":"","uid":""}},{"addr":"�����к��������峧·17��","cp":" ","direction":"��","distance":"440","name":"����������𽨲��̵�","poiType":"����","point":{"x":116.28925943497639,"y":39.972987921801209},"tag":"����;�Ҿӽ���","tel":"","uid":"61fa14618082975d3a04b1ea","zip":"","parent_poi":{"name":"","tag":"","addr":"","point":{"x":0.0,"y":0.0},"direction":"","distance":"","uid":""}},{"addr":"�����к������粨԰��1��","cp":" ","direction":"��","distance":"393","name":"�����(�粨԰��)","poiType":"��������","point":{"x":116.29353536920388,"y":39.97005038870725},"tag":"��������;����ά��","tel":"","uid":"af1abb69134d84ee92114c59","zip":"","parent_poi":{"name":"","tag":"","addr":"","point":{"x":0.0,"y":0.0},"direction":"","distance":"","uid":""}},{"addr":"�����к�������Ӫ��·����԰12��¥3-4��Ԫ1��","cp":" ","direction":"����","distance":"390","name":"�������֮ͯ��(�׶�԰)","poiType":"������ѵ","point":{"x":116.28750773923193,"y":39.96810117887099},"tag":"������ѵ;�׶�԰","tel":"","uid":"80a73b12e198d790774ff1fc","zip":"","parent_poi":{"name":"","tag":"","addr":"","point":{"x":0.0,"y":0.0},"direction":"","distance":"","uid":""}}],"roads":[],"poiRegions":[],"sematic_description":"�й���������(����Զ����·֧��)��102��","cityCode":131}}'
#     p1 = r"������.*��"
#     pattern1 = re.compile(p1)
#
#     print(pattern1.findall(my_txt)[0].split('������')[1].split('��')[0])
#





def gen_beijing_external_data(coor):
    all_point=coor['o']|coor['d']
    print(all_point)
    return 0


def gen_shanghai_external_data(coor):
    return 0


def gen_shenzhen_external_data(coor):
    return 0



beijing_feature=pd.read_csv('../feature_data/feature_beijing.csv')
gen_beijing_external_data(beijing_feature[['o','d']])

shanghai_feature=pd.read_csv('../feature_data/feature_shanghai.csv')
gen_shanghai_external_data(shanghai_feature[['o','d']])

shenzhen_feature=pd.read_csv('../feature_data/feature_shenzhen.csv')
gen_shenzhen_external_data(shenzhen_feature[['o','d']])