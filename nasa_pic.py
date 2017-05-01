from bs4 import BeautifulSoup
import urllib2
import urllib
import os

resp = urllib2.urlopen("https://apod.nasa.gov/apod/astropix.html")
soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
part=[]

for link in soup.find_all('a', href=True):
    print link['href']
    if link['href'].find('jpg' or 'png' or 'jpeg') != -1:
        part.append(link['href'])

image_link='https://apod.nasa.gov/apod/' + part[0]

urllib.urlretrieve(image_link, "local-filename.jpg")


os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/geek-house/NASA/local-filename.jpg")

