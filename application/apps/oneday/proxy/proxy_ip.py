
import urllib2

if __name__ =="__main__":
    with open('proxy_ip_guangdong.dat', 'r') as fi:
        for p in fi.readlines():
            p = p.strip()

            print p
            proxy_handler = urllib2.ProxyHandler({'https': p})

            opener = urllib2.build_opener(proxy_handler)
            try:
                req = urllib2.Request('http://1.oneday67.sinaapp.com')
                req.add_header('X-Forworded-For', '')
                content = opener.open(req, timeout = 5).read()
                print 'yes'
            except Exception as e:
                print e
                pass


