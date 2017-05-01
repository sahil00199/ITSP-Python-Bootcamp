from bs4 import BeautifulSoup
import urllib2
import urllib
import os
###Part 1: To get all the links available in the webpage
resp = urllib2.urlopen("https://apod.nasa.gov/apod/astropix.html")
soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
part=[]

for link in soup.find_all('a', href=True):
    print link['href']
    if link['href'].find('jpg' or 'png' or 'jpeg') != -1:     #To search for links having image format
        part.append(link['href'])

image_link='https://apod.nasa.gov/apod/' + part[0]        # To add the partial link with the pre part of the website

urllib.urlretrieve(image_link, "local-filename.jpg")     #To download and save the image as "local-filename.jpg"


#To change wallpaper in Ubuntu
os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/geek-house/NASA/local-filename.jpg")

