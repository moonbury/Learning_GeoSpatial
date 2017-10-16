# Retrieve a file using urllib
import urllib2 #.request
import urllib2#.parse
import urllib2#.error
url = "https://github.com/GeospatialPython/Learning/raw/master/hancock.zip"
fileName = "hancock.zip"
urllib.request.urlretrieve(url, fileName)
