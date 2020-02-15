#!/usr/bin/zsh
# to post to the eurobot 

t set active EurovizhnWisdom
tweet=`python ~/eurobot/euro_rand_140.py`
t update "$tweet"

# cron timing:
#0	0,8,16	*	*	*	sh ~/eurobot/eurorun.sh
