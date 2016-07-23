import urllib
import urllib2
from urlparse import urlparse
from bs4 import BeautifulSoup

def has_protocol(url):
    return url.startswith("http://") or url.startswith("https://")

def main():
    addr = raw_input("URL: ")
    if not has_protocol(addr):
        addr = "http://" + addr
    print "Opening page: %s" % addr

    page = urllib2.urlopen(addr)
    print "Page opened!"

    soup = BeautifulSoup(page, "lxml")
    links = map(lambda i: i.get("src"), soup.find_all("img")) # links to all images
    links = list(set(links)) # remove duplicates
    print "Found %d image(s)" % len(links)

    for link in links:
        if not has_protocol(link): # change relative links to absolute
            link = addr + '/' + link

        # download link
        print "Retrieving %s" % link
        path = urlparse(link).path
        name = path.split('/')[-1]
        urllib.urlretrieve(link, name)

if __name__ == '__main__':
    main()
