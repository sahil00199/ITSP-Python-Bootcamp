#!/usr/bin/python

import bs4 #to parse from the html code
#import webbrowser
import requests #to get the html code

def convert(word_list):
	ans = ""
	for object in word_list:
		ans+=object
		ans+="-"
	return ans[:-1] # to remove the extra "-" at the end.

if __name__ == "__main__":
	song = raw_input("Enter the name of a song: ").split()
	artist = raw_input("Enter the name of the artist: ").split()
	#We look at the site metorlyrics and see how the url of any song of any artist is represented
	# and try to generalise
	base = "http://www.metrolyrics.com/"
	end = ".html"
	#The name of a song that has more than one word is each word separated by a "-"...we create a function to do this
	#then the word "lyrics" and then the artist name in a similar manner.
	song = convert(song)
	artist = convert(artist)
	link = base+song+"-lyrics-"+artist+end
	html_response = requests.get (link) #get the html code
	html_code = ""
	for chunk in html_response.iter_content (100000):
		html_code+=chunk
	#store the html code in html_code
	soup = bs4.BeautifulSoup(html_code , "lxml") #make a bs4 object of the code
	song = soup.select('.verse') #go through the source code and find out where the lyrics are stored.
	#they are stored in a class called 'verse'. refer to the web scraping page on Wncc's wiki.
	for element in song:
		print(element.getText())