#!usr/bin/sh
# to post to the eurobot 
# this is to set the env properly
PATH=/usr/local/bin:/usr/local/sbin:~/bin:/usr/bin:/bin:/usr/sbin:/sbin

#tweet=`python ~/eurobot/euro_rand_140.py`
tweet=`cat tmptwt`
t update "$tweet"

# cron timing:
#0	0,8,16	*	*	*	sh ~/eurobot/eurorun.sh
