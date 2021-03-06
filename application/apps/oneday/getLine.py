#coding=utf-8
from random import randint
import urllib
import urllib2
#import pymongo
import re
import math
import json
#from xml.etree import ElementTree as ET
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import requests

dist_s = json.load(open(os.path.dirname(os.path.realpath(__file__)) + '/time_bak.dat', 'r'))

class Line:
    def __init__(self):
        #connection = pymongo.Connection(OPENSHIFT_ADR, 27017)
        #db = connection.oneday
        #self.flagset = set([])
        #self.items = []

        #self.class_cnt = 7
        #self.item_classes = [[] for _ in xrange(self.class_cnt)]
        #self.EAT, self.XIAOCHI, self.DRINK,self.JINDIAN, self.PLAY, self.KTK, self.OTHERS = xrange(self.class_cnt)
        #self.pattern = []
        #self.pattern.append(re.compile('豆皮|农家菜|粤菜|热干面|湘菜|卤味|东南亚菜|韩国料理|牛肉粉|比萨|西式简餐|火锅|川菜|烧烤|自助餐|湖北菜|小龙虾|汤包|日本料理|海鲜|牛排|快餐简餐|粉面馆|西餐'))
        #self.pattern.append(re.compile('零食|面包糕点|小吃'))
        #self.pattern.append(re.compile('甜品饮料|酒吧|咖啡厅|茶馆'))
        #self.pattern.append(re.compile('景点|郊游|公园|文化艺术|电影院'))
        #self.pattern.append(re.compile('台球室|游乐游艺|'))
        #self.pattern.append(re.compile('KTV'))
        #self.pattern.append(re.compile(''))
        #self.avedist = 0.0
        #self.place = None

        #for _ in db.items.find():
        #    self.flagset.add(_['flag'][0])
        #    self.items.append(_)
        #    for i in xrange(self.class_cnt):
        #        if re.findall(self.pattern[i], _['flag'][0].encode('utf-8')):
        #            self.item_classes[i].append(_)
        #            break


        return
        #for _ in self.flagset:
        #    print _

        #for i in self.item_classes:
        #    print len(i)
        #print '**********************************'

    #def itemType(self, item):
    #    #for i, pattern in enumerate(self.pattern):
    #    #    if re.findall(pattern, item['flag'][0].encode('utf-8')):
    #    #        return i
    #    #result = self.PLAY
    #    #s = item['flag'][0]
    #    #s = s.encode('utf-8')
    #    #if re.findall(self.eatPattern, s):
    #    #    result = self.EAT
    #    pass

    #    return result

    #def dist(a, b):
    #    result = 100
    #    if a.has_key('lat') and b.has_key('lat'):
    #        result = math.sqrt( (a['lat'] - b['lat']) ** 2 + (a['lng'] - b['lng']) ** 2 )
    #    return result


    cnt = 0

    #def getPlayLatlng():
    #    fi = open('res/play.dat', 'w')
    #    for i, itemplay in enumerate(self.items[1:]):
    #        for item in itemplay:
    #            if item.has_key('lat') and item['lat'] // 1 == 30.0 and item['lng'] // 1 == 114.0:
    #                fi.write(str(item['lat']) + ' '  + str(item['lng']) + ' ' + str(i) + '\r\n')
    #    fi.close()

    @staticmethod
    def isSameFlag(a, b):
        if a['flag'] == b['flag']:
            return 1
        if a['flag'].find('公园') != -1 and b['flag'].find('公园') != -1:
            return 1
        if a['flag'].find('景点') != -1 and b['flag'].find('景点') != -1:
            return 1
        if a['flag'].find('郊游') != -1 and b['flag'].find('郊游') != -1:
            return 1
        if a['flag'].find('文化') != -1 and b['flag'].find('文化') != -1:
            return 1
        if a['flag'].find('电影') != -1 and b['flag'].find('电影') != -1:
            return 1
        if a['name'].find('图书馆') != -1 and b['name'].find('图书馆') != -1:
            return 1

        if a['name'].find('剧院') != -1 and b['flag'].find('电影') != -1:
            return 1
        if b['name'].find('剧院') != -1 and a['flag'].find('电影') != -1:
            return 1



        if re.findall('书店|图书馆', a['flag'].encode('utf-8')) and re.findall('酒吧|KTV|台球室|桌面游戏|按摩|洗浴|电玩|游乐游艺', b['flag'].encode('utf-8')):
            return 1
        if re.findall('书店|图书馆', b['flag'.encode('utf-8')]) and re.findall('酒吧|KTV|台球室|桌面游戏|按摩|洗浴|电玩|游乐游艺', a['flag'].encode('utf-8')):
            return 1
        if re.findall('酒吧|KTV|台球室|桌面游戏|按摩|洗浴|电玩|游乐游艺', a['flag'].encode('utf-8')):
            if re.findall('文化|艺术', b['flag'].encode('utf-8')) and not re.findall('class', b['tags'].encode('utf-8')):
                return 1
        if re.findall('酒吧|KTV|台球室|桌面游戏|按摩|洗浴|电玩|游乐游艺', b['flag'].encode('utf-8')):
            if re.findall('文化|艺术', a['flag'].encode('utf-8')) and not re.findall('class', a['tags'].encode('utf-8')):
                return 1

        return 0

    @staticmethod
    def item_one_condition(item):
        if re.findall('电影|酒吧|洗浴|按摩', item['flag'].encode('utf-8')):
            return 0
        if re.findall('剧院', item['name'].encode('utf-8')):
            return 0
        if re.findall('KTV'.encode('utf-8'), item['flag'].encode('utf-8')):
            return 0
        return 1

    @staticmethod
    def item_two_condition(item):
        if re.findall('酒吧|洗浴|按摩', item['flag'].encode('utf-8')):
            return 0
        return 1

    @staticmethod
    def item_three_condition(item):
        #return 1 if randint(0, 100) < 1 else 0
        return 1

    @staticmethod
    def dist_latlng(a, b):
        R = 6371.004
        C = math.sin(a['lat']) * math.sin(b['lat']) * math.cos(a['lng'] - b['lng']) + math.cos(a['lat']) * math.cos(b['lat'])
        C = 1.0 if C > 1.0 else C
        return R * math.acos(C) *math.pi / 180

    @staticmethod
    def get_shortest_item(lat, lng):
        #play = pymongo.Connection(OPENSHIFT_ADR, 27017).oneday.play.find()
        #play = [_ for _ in play]
        fi = open(os.path.dirname(os.path.realpath(__file__)) + '/oneday.play.json', 'r')
        play = json.load(fi)
        play = play["play"]
        Min = []
        for b in play:
            try:
                R = 6371.004
                C = math.sin(lat) * math.sin(b['lat']) * math.cos(lng - b['lng']) + math.cos(lat) * math.cos(b['lat'])
                if R * math.acos(C) *math.pi / 180 < 10:
                    Min.append(b)
                #else: print R * math.acos(C) * math.pi
            except:
                print 'erro'
        fi.close()
        return Min

    def getTime(a, b):
        result = 100
        a = urllib.quote(str(a['lat']) + ',' + str(a['lng']))
        b = urllib.quote(str(b['lat']) + ',' + str(b['lng']))
        url = 'https://maps.googleapis.com/maps/api/directions/json?origin='+a+'&destination='+b+'&sensor=false&language=zh_cn&region=cn'
        req = urllib2.Request(url)
        req = urllib2.urlopen(url)
        req = json.load(req)
        try:
            print req['routes'][0]['legs'][0]['distance']['text'].split(' ')[0]
        except:
            print req

        return result

    def get_map(a, b):
        result = 100
        a = urllib.quote(str(a['lat']) + ',' + str(a['lng']))
        b = urllib.quote(str(b['lat']) + ',' + str(b['lng']))
        url = 'https://maps.googleapis.com/maps/api/directions/json?origin='+a+'&destination='+b+'&sensor=false&language=zh_cn&region=cn'
        req = urllib2.Request(url)
        req = urllib2.urlopen(url)
        req = json.load(req)
        return req

    #def get_eat_count(item):
    #    cnt = 0
    #    for _ in self.item_classes[0]:
    #        if dist_latlng(item, _) < 0.5:
    #            cnt += 1

    #    return cnt

    def decodePoly(encode):
        print encode
        res = []
        index = 0
        lat = 0
        lng = 0
        cnt = 0
        while index < len(encode):
            shift = 0
            result = 0
            while index < len(encode):
                b = ord(encode[index]) - 63
                index += 1
                result |= (b & 0x1f) << shift
                shift += 5
                if (b < 0x20):
                    break
            dlat =  ~(result >> 1) if (result & 1) != 0  else result >> 1
            lat += dlat;

            shift = 0
            result = 0
            while index < len(encode):
                b = ord(encode[index]) - 63
                index += 1
                result |= (b & 0x1f) << shift
                shift += 5
                if (b < 0x20):
                    break
            dlng =  ~(result >> 1) if (result & 1) != 0  else result >> 1
            lng += dlng;
            res.append((lat, lng))
            res = [str(_) for _ in res]
            cnt += 1
            if cnt > 10000: return res
        return res

    #def get_time(start_lat, start_lng, end_lat, end_lng):
    #    url = 'http://openapi.aibang.com/bus/transfer?app_key=f41c8afccc586de03a99c86097e98ccb&city=%E6%AD%A6%E6%B1%89&start_lat='+start_lat+'&start_lng='+start_lng+'&end_lat='+end_lat+'&end_lng='+end_lng
    #    result = urllib2.urlopen(url)
    #    xml_root = ET.fromstring(result.read())
    #    buses = xml_root.find('buses')
    #    if not buses:
    #        L = math.sqrt(math.pow(float(start_lat) - float(end_lat), 2) + math.pow(float(start_lng) - float(end_lng), 2))
    #        if L < 0.02:
    #            return {'dist':0, 'time':0, 'foot_dist':0, 'last_foot_dist':0, 'segs':""}
    #        else :
    #            return {'dist':1000000, 'time':1000000, 'foot_dist':10000000, 'last_foot_dist':10000000, 'segs':""}
    #    dist = buses[0][0].text
    #    time = buses[0][1].text
    #    foot_dist = buses[0][2].text
    #    last_foot_dist = buses[0][3].text
    #    segments = buses[0][4].findall('segment')
    #    segs = []
    #    for seg in segments:
    #        segs.append({'start_stat':seg[0].text, 'end_stat':seg[1].text, 'line_name':seg[2].text, 'stats':seg[3].text})
    #    res = {'dist':dist, 'time':time, 'foot_dist':foot_dist, 'last_foot_dist':last_foot_dist, 'segs':segs}
    #    #print res
    #    return res

    def get_bus_time(self, name_1, name_2):
        global dist_s
        try:
            ret = dist_s[name_1.decode('utf-8') + ' ' + name_2.decode('utf-8')]
        except:
            ret = dist_s[name_2.decode('utf-8') + ' ' + name_1.decode('utf-8')]
        return ret

    def getline(self, lat, lng, begin, end, item_all_condition = lambda x: 1):
        #play = pymongo.Connection(OPENSHIFT_ADR, 27017).oneday.play.find()
        fi = open(os.path.dirname(os.path.realpath(__file__)) + "/oneday.play.json", 'r')
        play = json.load(fi)
        play = play["play"]
        #dist_s = json.load(open(OPENSHIFT_DIR + 'application/apps/oneday/time_bak.dat', 'r'))
        global dist_s
        cnt = 0
        #play = [_ for _ in play]
        lines = []
        one_s = []
        two_s = []
        three_s = []

        for i in play:
            if Line.item_one_condition(i):
                one_s.append(i)

        import time as Time
        one_s = Line.get_shortest_item(float(lat), float(lng))
        start_time = Time.time()

        while cnt < end - begin and Time.time() - start_time < 5:
            try:
                one = one_s[randint(0, len(one_s) - 1)]
            except:
                return json.dumps("{'result':'error lat or lng'}")

            for i in play:
                if not Line.isSameFlag(one, i) and Line.item_two_condition(i):
                    try:
                        dist = dist_s[i['name'] + ' ' + one['name']]
                    except:
                        try:
                            dist = dist_s[one['name'] +' ' + i['name']]
                        except:
                            pass
                    if int(dist) == -1 and Line.dist_latlng(i, one) > 15:
                        dist = 1000
                    elif int(dist) > 1000:
                        dist = -1

                    if dist and int(dist) < 30:
                        two_s.append(i)
            if len(two_s) == 0:
                continue

            two = two_s[randint(0, len(two_s) - 1)]

            #if int(one['time']) + int(two['time']) >= 120:
            #    cnt += 1
            #    lines.append([one, two])
            #    print cnt ,lines[len(lines) - 1]
            #    continue

            for i in play:
                if not Line.item_three_condition(i):continue
                if Line.isSameFlag(one, i) or Line.isSameFlag(two, i):continue
                flag = 1 if re.findall('咖啡厅|茶馆', one['flag'].encode('utf-8')) else 0
                flag += 1 if re.findall('咖啡厅|茶馆', two['flag'].encode('utf-8')) else 0
                flag += 1 if re.findall('咖啡厅|茶馆|酒吧', i['flag'].encode('utf-8')) else 0
                if (flag > 1):continue
                if int(one['time']) + int(two['time']) + int(i['time']) > 200:continue
                #dist_one_three = get_time(str(one['lat']), str(one['lng']), str(three['lat']), str(three['lng']))
                #dist_two_three = get_time(str(two['lat']), str(two['lng']), str(three['lat']), str(three['lng']))

                try:
                    dist_one_three = dist_s[i['name'] + ' ' + one['name']]
                except:
                    try:
                        dist_one_three = dist_s[one['name'] + ' ' + i['name']]
                    except:
                        pass
                if int(dist_one_three) == -1 and Line.dist_latlng(i, one) > 15:
                    dist_one_three = 1000
                elif int(dist) > 1000:
                    dist = -1

                try:
                    dist_two_three = dist_s[i['name'] + ' ' + two['name']]
                except:
                    try:
                        dist_two_three = dist_s[two['name'] + ' ' + i['name']]
                    except:
                        pass
                if int(dist_two_three) == -1 and Line.dist_latlng(i, two) > 15:
                    dist_two_three = 1000
                elif int(dist) > 1000:
                    dist = -1

                if not dist_one_three or not dist_two_three:
                    continue
                #if dist_latlng(one, three) < dist_latlng(one, two) or dist_latlng(two, three) > 7:continue

                if int(dist_one_three) < int(dist_two_three) * 2 or int(dist_two_three) > 35:continue
                if not item_all_condition([one, two, i]): continue;
                if i['flag'].encode('utf-8').find('书'.encode('utf-8')) != -1: continue
                three_s.append(i)
                pass
            if len(three_s) == 0:
                continue
            three = three_s[randint(0, len(three_s) - 1)]
            lines.append([one, two, three])
            #print dist_one_three, dist_two_three
            cnt += 1
            #print cnt, lines[len(lines) - 1]

        #print self.get_bus_time(lines[0][0]['name'], lines[0][2]['name']) , self.get_bus_time(lines[0][1]['name'], lines[0][2]['name'])
        if cnt < end - begin:
            return None
        lines = [Line.getList(lat, lng, i[0], i[1], i[2]) for i in lines]
        fi.close()
        return json.dumps(lines)


    @staticmethod
    def find_one(q):
        with open(os.path.dirname(os.path.realpath(__file__)) + '/oneday.play.json', 'r') as fi:
            play = json.load(fi)['play']
            for i in play:
                for k in q.keys():
                    if i[k] == q[k].decode('utf-8'):
                        return i
        return None

    @staticmethod
    def get_bus_human(namea = None, nameb = None, lat = None, lng = None):
        url_pre = 'http://busapi.sinaapp.com/?start_lat='
        if namea: p = Line.find_one({'name': namea})
        if nameb: n = Line.find_one({'name': nameb})
        if lat and lng:
            if namea:
                url = (url_pre
                    +str(p['lat'])+'&start_lng='+str(p['lng'])+'&end_lat='+str(lat)+'&end_lng='+str(lng)+'&alt=json')
            elif nameb:
                url = (url_pre
                    +str(lat)+'&start_lng='+str(lng)+'&end_lat='+str(n['lat'])+'&end_lng='+str(n['lng'])+'&alt=json')
        else:
            url = (url_pre
                +str(p['lat'])+'&start_lng='+str(p['lng'])+'&end_lat='+str(n['lat'])+'&end_lng='+str(n['lng'])+'&alt=json')
        _bus = json.loads(requests.get(url).content)
        if not _bus:
            s = u'没有公交或步行可达'
            return s

        '''
        s = ''
        t = _bus['transfers'][0]
        if not type(t['lines']) == type([]):
            s += t['lines']['name'] + '\t\n'
            s += u'全程总长' + t['distance'] + '\t\n'
            s += u'途径站数'  + t['lines']['stop_num'] + '\t\n'
        else:
            for l in t['lines']:
                print '***',l
                s += u'全程总长' + l['distance'] + '\t\n'
                s += u'途径站数'  + l['stations_num'] + '\t\n'
        '''

        try:
            #之前调用aibang的api的，现在改成用自己的api
            '''
            s = ''
            for index in xrange(len(_bus['buses']['bus'][0]['segments']['segment'])):
                t = _bus['buses']['bus'][0]['segments']['segment'][index]
                s += '步行' + t['foot_dist'] + '米至'  + t['start_stat'] + '\n'
                s += '搭乘' + t['start_stat'] + '  经过' + t['stats'] + ' 到达' + t['end_stat']
                s += '\n'
            '''
            s = ''
            t = _bus['transfers'][0]
            if not type(t['lines']) == type([]):
                s += t['lines']['name'] + '\t\n'
                s += u'全程总长' + t['distance'] + '\t\n'
                s += u'途径站数'  + t['lines']['stop_num'] + '\t\n'
            else:
                for l in t['lines']:
                    print '***',l
                    s += u'全程总长' + l['distance'] + '\t\n'
                    s += u'途径站数'  + l['stations_num'] + '\t\n'
        except Exception as e:
            print e
            s = "没有公交或者距离很近步行可达"
        return s

    @staticmethod
    def getList(lat, lng, one, two, three):
        #play = pymongo.Connection(OPENSHIFT_ADR, 27017).oneday.play.find()
        #play = [_ for _ in play]
        #length = len(play)
        #ret = []
        #cnt = end - begin
        #one = play[randint(0, length - 1)]
        #two = play[randint(0, length - 1)]
        #three = play[randint(0, length - 1)]
        url = "http://api.map.baidu.com/staticimage?"
        url += "markers=" + str(one['lng']) + ',' + str(one['lat']) + '|'
        url += str(two['lng']) + ',' + str(two['lat']) + "|"
        url += str(three['lng']) + ',' + str(three['lat'])
        url += "&markerStyles=A|m,B|l,C"
        minLat = min(one['lat'], two['lat']); minLat = min(minLat, three['lat'])
        minLng = min(one['lng'], two['lng']); minLng = min(minLng, three['lng'])
        maxLat = max(one['lat'], two['lat']); maxLat = max(maxLat, three['lat'])
        maxLng = max(one['lng'], two['lng']); maxLng = max(maxLng, three['lng'])
        height = (maxLat - minLat) / (maxLng - minLng) * 480
        centerLat = (maxLat + minLat) / 2.0
        centerLng = (maxLng + minLng) / 2.0
        url += "&bbox=" + str(minLng) + ',' + str(minLat) + ';' + str(maxLng) + ',' + str(maxLat)
        #url += "&width=480&height=" + str(height)
        url += "&width=300&height=300"
        url += "&paths=" + str(one['lng']) + ',' + str(one['lat']) + ';'
        url += str(two['lng']) + ',' + str(two['lat']) + ";"
        url += str(three['lng']) + ',' + str(three['lat'])
        url += "&center=" + str(centerLng) + ',' + str(centerLat)
        pos = []
        pos.append( (round(height / 2.0 - (one['lat'] - centerLat) * height / (maxLat - minLat)),
                round(240 + (one['lng'] - centerLng) * 480 / (maxLng - minLng))) )
        pos.append(( round(height / 2.0 - (two['lat'] - centerLat) * height / (maxLat - minLat)),
                round(240 + (two['lng'] - centerLng) * 480 / (maxLng - minLng))) )
        pos.append(( round(height / 2.0 - (three['lat'] - centerLat) * height / (maxLat - minLat)),
                round(240 + (three['lng'] - centerLng) * 480 / (maxLng - minLng))))
        json_one = {}
        json_two = {}
        json_three = {}

        for item , item_json in zip([one, two, three], [json_one, json_two, json_three]):
            if not three:
                break

            for i in item.keys():
                if i != '_id':
                    if type(item[i]) == type(123.4324234) or str(item[i]).isdigit():
                        item_json[i] = str(item[i])
                    else:
                        item_json[i] = item[i]

            Map = ("http://api.map.baidu.com/staticimage?markers=" + str(item['lng']) + ',' + str(item['lat'])
                + "&center=" + str(item['lng']) + ',' + str(item['lat'])  )
            item_json['map'] = Map

            if item_json['img'] != []:
                continue
            urll = 'http://www.dianping.com/search/keyword/16/0_' + urllib.quote(item_json['name'].encode('utf-8'))
            content = requests.get(urll).content
            #shopId = re.findall('shopIDs:\t\[(.*)\],\r', content)[0].split(',')
            shopId = re.findall('shopIDs:.*\[(.*)\],', content)[0].split(',')

            urll = 'http://www.dianping.com/shop/'+ shopId[0] +'/photos'
            pattern = 'http://i[0-9].s[0-9].dpfile.com/pc/[0-9a-z()]*/thumb.jpg'
            content = requests.get(urll).content
            img = re.findall(pattern ,content)[:8]
            #Map = ("http://api.map.baidu.com/staticimage?markers=" + str(item['lng']) + ',' + str(item['lat'])
            #    + "&center=" + str(item['lng']) + ',' + str(item['lat'])  )
            item_json['img'] = img
            #item_json['map'] = Map

        '''
        for i in one.keys():
            if i != '_id':
                json_one[i] = one[i]

        for i in two.keys():
            if i != '_id':
                json_two[i] = two[i]

        for i in three.keys():
            if i != '_id':
                json_three[i] = three[i]
        '''



        '''
        line = {
                #"pos": pos,
                #"loc":[(one['lat'], one['lng']), (two['lat'], two['lng']), (three['lat'], three['lng'])],
                "img":url,
                #"name": str(one['name']) + '-' + str(two['name']) + '-' + str(three['name']),
                "items":[json_one, json_two, json_three],
                "linename": json_one['name'] + '__' +  json_two['name'] + '__' + json_three['name']
                }
        '''
        line = {
                #"pos": pos,
                #"loc":[(one['lat'], one['lng']), (two['lat'], two['lng']), (three['lat'], three['lng'])],
                "map":url,
                "place_1": json_one,
                "place_2": json_two,
                "place_3": json_three,
                "name": json_one['name'] + '__' +  json_two['name'] + '__' + json_three['name'],
                "bus": Line.get_bus_human(nameb = json_one['name'], lat = lat, lng = lng)
                        + '__' + Line.get_bus_human(namea = json_one['name'], nameb = json_two['name'])
                        + ('__' + Line.get_bus_human(namea = json_two['name'] if three else None, nameb = json_three['name'] if three else None) )
                        + '__' + Line.get_bus_human(namea = json_three['name'] if three else json_two['name'], lat = lat, lng = lng)
                }
        #ret.append(line)
        return line
        #return json.dumps(ret)

if __name__ == '__main__':
    line = Line()
    print line.getline('30.599133','114.290742',0,1)
