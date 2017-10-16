# Extract a zipped shapefile via a url
import urllib2
import urllib2
import urllib
import zipfile
import io
import struct

url = "https://github.com/GeospatialPython/Learning/raw/master/hancock.zip"
cloudshape = urllib2.urlopen(url)
memoryshape = io.BytesIO(cloudshape.read())
zipshape = zipfile.ZipFile(memoryshape)
cloudshp = zipshape.read("hancock.shp")
# Access Python string as an array
print(struct.unpack("<dddd", cloudshp[36: 68]))
