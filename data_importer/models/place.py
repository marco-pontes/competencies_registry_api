from data_importer.models.entity import *


class Place(db.Entity):
    def __init__(self, name, latitude, longitude, postal_code, region, street_address, country, locality):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.postal_code = postal_code
        self.region = region
        self.street_address = street_address
        self.country = country
        self.locality = locality

















#   "ceterms:address": [
#     {
#       "@type": "ceterms:Place",
#       "ceterms:name": {
#         "en": "Credential Engine Administration"
#       },
#       "ceterms:latitude": 37.7148936,
#       "ceterms:longitude": -89.2303154,
#       "ceterms:postalCode": "62901",
#       "ceterms:addressRegion": {
#         "en": "Illinois"
#       },
#       "ceterms:streetAddress": {
#         "en": "2450 Foundation Dr"
#       },
#       "ceterms:addressCountry": {
#         "en": "United States"
#       },
#       "ceterms:addressLocality": {
#         "en": "Springfield"
#       }
#     }
#   ],