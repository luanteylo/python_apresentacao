import httplib2
import urllib2
from BeautifulSoup import BeautifulSoup, SoupStrainer
import threading


url_name = 'http://lelivros.love/book/page/'
http = httplib2.Http()



def download_book(url, file_name):
    try:
        u = urllib2.urlopen(url)
        f = open("books/"+file_name, 'wb')
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
        
count = 1
url_name = 'http://lelivros.website/book/page/'+str(count)

while count < 317:
    status, response = http.request(url_name)
    jobs = []
    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('rel'):
            book_link = link.attrMap['href']
            if book_link.find("page") == -1:
                #print book_link
                st, resp = http.request(book_link)
                tree = BeautifulSoup(resp)
                url = tree.findAll(attrs={'rel':"nofollow", 'target':"_blank"})[1].attrMap['href']
                file_name = urllib2.unquote(url).split(".com")[-1].replace("/"," ")
                jobs.append(threading.Thread(target=download_book, args=[url, file_name]))
                jobs[-1].start()
                #download_book(url, file_name)
            else:
                print "Next page...", book_link
                url_name = book_link

    else:
        count += 1
        for i in jobs:
            i.join()
