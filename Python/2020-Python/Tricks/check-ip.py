import urllib
import re

print ("We will try to open this URL in order to get the IP address.")
url = "http://checkip.dydns.org"

print (url)

request = urllib.urlopen(url).read()
theIP = re.findall(r"d{1,3}.d{1,3}.d{1,3}.d{1,3}", request)

print ("Your IP address is: ",theIP)