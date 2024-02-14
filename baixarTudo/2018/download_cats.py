import httplib2
import urllib2
from BeautifulSoup import BeautifulSoup, SoupStrainer
import threading


url_name = 'https://cantodosgatinhos.blogspot.com/p/lindas-fotos-de-gatos.html'
http = httplib2.Http()



def download(url, file_name):
    try:
        u = urllib2.urlopen(url)
        f = open("cats/"+file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            # status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            # status = status + chr(8)*(len(status)+1)
            # print status,
        f.close()
    except:
        print "Broken link", file_name
        


status, response = http.request(url_name)

soup =  BeautifulSoup(response)

# print dir(soup)

for a in soup.findAll('img', src=True):
    link =  "https:" + a['src']

    if link.find('.jpg') != -1:
        file_name =  link.split('/')[-1]
        download(link, file_name)

