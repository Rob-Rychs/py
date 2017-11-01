from pygeocoder import Geocoder

address = input("Enter your address: ")

try:
    print (Geocoder.geocode(address)[0].coordinates)
except:
    print ("Error: Can't find, please try again.")
