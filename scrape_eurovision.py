# scrape eurovision for lyrics, archive as a hash.
# max 8/27/2014

# updated 2015 to spoof eurovision site- they put up a system to read url request headers

import sys
import pickle
import urllib2
import re

# a class to contain metadata about songs? maybe in a fancier version.
#class Song(object):
#	def __init__(self,title, performer,year,country,lyrics):
#		self.performer = performer
#		self.year = year
#		self.country = country
#		self.title = title
#		self.lyrics = lyrics
#	def getLyrics(self):
#		return lyrics
#	def getTitle(self):
#		return title
#### ....etc.
#### finish up sometime.


#req2015 = urllib2.Request('http://www.eurovision.tv/page/history/by-year/contest?event=2083', headers={'User-Agent' : "Magic Browser"})

root_url = 'http://www.eurovision.tv/'

print 'requesting access'
# just add header to requests --> works
year_req = urllib2.Request(root_url+'page/history/year', headers={'User-Agent' : "Magic Browser"})
print 'reading'
year_page = urllib2.urlopen(year_req).read()

contest_pat = re.compile(r'page/history/by-year/contest\?event=([0-9]+)')
contest_list = set(re.findall(contest_pat,year_page))

song_hash = {}

song_pat = re.compile(r'/page/history/year/participant-profile/\?song=([0-9]+)')
lyrics_pat = re.compile(r'<p class="lyrics lyrics-ltr" style="direction:ltr">([.]+)</p>')


for contest in contest_list:
	print contest
	req = urllib2.Request(root_url+'page/history/by-year/contest?event='+contest, headers={'User-Agent' : "Magic Browser"})
	page = urllib2.urlopen(req).read()
	songs = set(re.findall(song_pat,page))
	print contest,len(songs)
	for song in songs:
		lyric_req = urllib2.Request(root_url+'event/lyrics?event=' + contest + '&song='+song, headers={'User-Agent' : "Magic Browser"})
		lyric_page = urllib2.urlopen(lyric_req).read()

		print lyric_page.replace('<br/>',' ')
		song_hash[song] = lyric_page.replace('<br/>',' ')

outfile = open('eurovision_lyrics_2015.pkl','wb')
pickle.dump(song_hash,outfile)

print len(song_hash.keys())

# at some point, add a section to scrape the rankings, scores, and song ids
# to do analytics??
