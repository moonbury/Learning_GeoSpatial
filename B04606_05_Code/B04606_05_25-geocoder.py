"""Geocode with Geocoder"""

import geocoder
#g = geocoder.google("1403 Washington Ave, New Orleans, LA 70130")
g = geocoder.google("38 Sung Wong Toi Road, To Kwa Wan, Kowloon, Hong Kong")
print(g.geojson)
print()
print(g.wkt)
