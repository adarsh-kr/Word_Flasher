import pynotify 
import sys
import urllib2
from bs4 import *
import random
from random import randint
from time import sleep


pynotify.init(sys.argv[0])
print(sys.argv[0])


proxy = urllib2.ProxyHandler({'http': 'http://k.adarsh:boobs@202.141.80.20:3128'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)

word_file=open('words','r')
list_of_words=word_file.read().splitlines()

num_of_word=len(list_of_words)
num_of_word_to_present=random.sample(xrange(num_of_word), 10)
#print num_of_word_to_present
k=0
while (1):

	if(k==10):
		num_of_word_to_present=random.sample(xrange(num_of_word), 10)
		print num_of_word_to_present		
		k=0
		
	word_to_present=list_of_words[num_of_word_to_present[k]]

	print(word_to_present)
	
	data=urllib2.urlopen('http://www.vocabulary.com/dictionary/'+word_to_present)
	soup=BeautifulSoup(data)
	
	x=soup.find('p',{'class':'long'})
	y=soup.find('p',{'class':'short'})
	if(x!=None):	
		x=soup.find('p',{'class':'long'}).get_text()
	else :
		x='Not in Vocab'
	if(y==None):
		y='Not in Vocab'
	else :
		y=y.get_text()

	
	notification=pynotify.Notification(word_to_present,y+'\n\n\n\n'+x)
	notification.set_urgency(pynotify.URGENCY_NORMAL)
	notification.set_timeout(pynotify.EXPIRES_NEVER)
	notification.show()
	#pynotify.Notification.props.icon_name='Final_Plot.jpg'
	#notification.show()
	k=k+1
	sleep(100)
