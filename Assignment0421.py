# -*- coding: utf-8 -*-
import json   # 解析 json 格式用的
import requests  # 用來上網抓取資料用的

url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=1000"

data = requests.get(url)   # 是stream  串流資料 bytes 位元組

bike = data.text  # 將串流資料轉換成文字內容

content = json.loads(bike) # 將文字格式帶入轉成  json 格式
#content 是json 格式


sareaList = []

for row in content:
    # print("區別:", row['sarea'])
    sareaList.append(row['sarea'])
# print(sareaList)




while True:
    bikeArea = []
    area = input("請輸入欲查詢的區別 輸入E離開")
    if area=='E':
        break
    if area in sareaList:
        print(area,'Ubike 資訊如下:')
        for item in content:
            if item['sarea']==area:
                bikeArea.append(item)
                print("站名: {} {}\t總數量: {}\t可借: {}\t可停: {}".format(item['sna'],item['snaen'],item['tot'],item['sbi'],item['bemp']))
        print('共有',len(bikeArea),'個據點')     
    if area not in sareaList:
        print('您輸入的區域查無資料')   