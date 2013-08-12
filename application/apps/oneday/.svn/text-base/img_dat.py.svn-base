

import json
import urllib
import requests
import re
import time


import threading
import Queue

queue = Queue.Queue()

class spider(threading.Thread):
    def __init__(self, queue, proxy):
        super(self, spider).__init__()
        self.queue = queue
        self.proxy = proxy

    def run(self):
        pass


if __name__ == "__main__":
    with open('./oneday.play.json', 'r') as fi:
        play = json.load(fi)['play']
        with open('./oneday.play.json_1', 'r') as ff:
            ret = json.load(ff)['play']
        cnt = 0
        s = requests.Session()
        for item_json in ret:
            print cnt
            if cnt and cnt % 10 == 0:
                time.sleep(4)
            cnt += 1
            if item_json['img'] != []:
                continue
            try:
                url = 'http://www.dianping.com/search/keyword/16/0_' + urllib.quote(item_json['name'].encode('utf-8'))
                content = s.get(url).content
                shopId = re.findall('shopIDs:\t\[(.*)\],\r', content)[0].split(',')

                url = 'http://www.dianping.com/shop/'+ shopId[0] +'/photos'
                pattern = 'http://i[0-9].s[0-9].dpfile.com/pc/[0-9a-z()]*/thumb.jpg'
                content = s.get(url).content
                img = re.findall(pattern ,content)
                img = list(set(img))
                img = img[:8]

                item_json['img'] = img
                print item_json, '\n'
            except Exception as e:
                print e, 'error', '\n'
                item_json['img'] = []
            with open('./oneday.play.json_2', 'w') as fff:
                fff.write(json.dumps({"play": ret}))
