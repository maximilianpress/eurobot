# to load the eurovision song-hash object and return a string of lyrics of <140 chars
# of full lines

# updated for 2015 contest

import random
import sys
import pickle
import re

file = open('eurobot/eurovision_lyrics_2016.pkl','rb')
#file = open('eurobot/eurovision_lyrics_2015.pkl','rb')
song_hash = pickle.load(file)
num_lines = 0
#hashtag = ' #eurovision2015'
hashtag = ''

while num_lines < 10:
	# choose song at random
	song_key = random.sample(song_hash.keys(),1)[0]
	# give it another chance to be random
	if random.random() < 0.5:
		continue
	quot_pat = re.compile(r'&[rl]squo;')
	song = re.sub(quot_pat,"'",song_hash[song_key])
	quot_pat = r"\,"
	song = re.sub(quot_pat,"",song)
	songy = song

	pat = re.compile(r'style=\"direction:ltr">[\w\n \'\\\.,;]+')
	pat = re.compile(r'style=\"direction:ltr">([\w\n \-\\\'\\\.,;]+)')

	song = re.findall(pat,song)[0]
	lines = song.split('\n')

	num_lines = len(lines)

rand = random.sample(range(num_lines),1)[0]

while rand >= (num_lines-4):
	rand = random.sample(range(num_lines),1)[0]

str = ''
for line in range(rand,num_lines):
	if lines[line] == ' ' or lines[line] == '':
		continue
	addition = lines[line].strip()
	if addition.startswith('Chorus') or addition.startswith('Verse'):
		continue
	newstr = str + ' \\ ' + addition
	if len(newstr+hashtag) >= 140:
		break
	str = newstr

print "'"+str[3:]+"'"+hashtag
