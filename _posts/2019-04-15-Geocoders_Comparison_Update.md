---
title: "Geocoders Comparison Update"
date: 2019-04-15
tags: [Data Visualization, GIS, folium]
excerpt: "Discovering the geocoding quirks in Nominatim, GoogleV3, ArcGis and AzureMaps APIs: September, 2018 vs. April, 2019 results."
---

# Comparison of four geocoders: Nominatim, GoogleV3, ArcGis and AzureMaps

## Geocoding services (via Geopy):

Obtaining the geolocation coordinates of a location specified by query string can be achieved using calls to geocoding APIs directly in a browser address box, or with
a wrapping library such as [geopy](https://geopy.readthedocs.io/en/stable/).

#### Here are the links to the geocoders geopy documentation and their respective service providers:
*  [**Nominatim**](https://geopy.readthedocs.io/en/stable/#Nominatim): [OpenStreetMaps](https://wiki.openstreetmap.org/wiki/Using_OpenStreetMap)
*  [GoogleV3](https://geopy.readthedocs.io/en/stable/#googlev3): [Google Map & Places API](https://developers.google.com/maps/documentation/geocoding/start)
*  [ArcGis](https://geopy.readthedocs.io/en/stable/#ArcGis): [ERSI ArcGIS API](https://developers.arcgis.com/rest/geocode/api-reference/overview-world-geocoding-service.htm)
*  [AzureMaps](https://geopy.readthedocs.io/en/stable/#azuremaps): [Microsoft Azure Maps API](https://docs.microsoft.com/en-us/azure/azure-maps/index)


## Why I setup this comparison:
In another application, I was using the New York City boroughs bounding boxes to impute missing borough names for records with geolocation information. 
The most expert GIS users among you would certainly predict scattershot results from such a "corner-cutting" approach, but initially I thought mine was a brilliant way to prevent over 85,000 requests... After I found out about the official territorial boundaries (shapefiles), I trashed the box solution!  

Yet, in the intervening time I had checked several services for speed and limits and I found out response differences between some geocoders...for the same query, so I investigated!

The [**Procedures notebook**](https://github.com/CatChenal/Geocoders_Comparison/notebooks/Procedures.ipnyb) shows how to retrieve the data and functions.

# The main conclusion from this comparison:  
I presume that it is very unlikely that an application would use different geolocating services, but in the case some 'hedging' is involved (e.g. on limits, time-outs), the geolocation for the same query will be different.
Additionally, my non-exhaustive comparison of four Geopy geocoders (out of 21), reveals that the boxing of a location is not always principled. For instance, Nominatim and GoogleV3 most often use the shapefile with water extent for boxing, whereas ArcGis and AzureMaps do not; moreover, ArcGis boxes typically extend further North than warranted by the existing shapefiles by at most 10 miles.  

# Update: Results &mdash;not the code&mdash; have changed!

When I rerun the geocoders comparison earlier this month (April, 2019), I found out differences in the results. The temporal report between the results from September, 2018 and those from April, 2019 can be viewed side by side in this HTML report implmented with a CSS slider:  

<a href="{{ site.url }}/assets/sliderReport.html" target="_blank">slider Report</a>

I've implemented the "sliderReport.html" by modifying a ["JS-less CSS slider"](https://github.com/drygiel/csslider) designed by GH user drygiel"  
Thank you, drygiel!

[Github repo](https://github.com/CatChenal/Geocoders_Comparison)
