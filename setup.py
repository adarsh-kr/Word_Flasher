import urllib2
if __name__ == "__main__":
	proxy = urllib2.ProxyHandler({'http': 'http://k.adarsh:astala@202.141.80.20:3128'})
	auth = urllib2.HTTPBasicAuthHandler()
	opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
	urllib2.install_opener(opener)
	print "Done :) \n"
