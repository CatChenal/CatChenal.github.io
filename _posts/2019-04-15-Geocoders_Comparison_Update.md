---
title: "Geocoders Comparison"
date: 2019-04-15
tags: [Data Visualization, GIS, folium]
excerpt: "Discovering the geocoding quirks &mdash; a polite characterization&mdash; in Nominatim, GoogleV3, ArcGis and AzureMaps APIs."
---

# Comparison of four geocoders: Nominatim, GoogleV3, ArcGis and AzureMaps# Comparison of Four Geocoders: Nominatim, GoogleV3, ArcGis and AzureMAps

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
The most expert GIS users among you would certainly predict scattershot results from such a "corner-cutting" approach, but initially I thought mine was a brilliant way to prevent over 85,000 requests...
After I found out about the official territorial boundaries (shapefiles), I trashed the box solution!  

Yet, in the intervening time I had checked several services for speed and limits and I found out response differences between some geocoders...for the same query, so I investigated!

The [**Procedures notebook**](https://github.com/CatChenal/Geocoders_Comparison/notebooks/Procedures.ipnyb) shows how to retrieve the data and functions.

# The main conclusion from this comparison:
Depending on the geolocating service used AND the location queried, the geolocation coordinates will be WRONG. 

## Following is the complete report: 
[notebook viewer](https://nbviewer.jupyter.org/github/CatChenal/Geocoders_Comparison/blob/master/GeocodersComparison/report/Report.ipynb)


# Update:

I found out differences in the results when I rerun the comaprison: the temporal report between the data from April, 2019 and September 2018 can be viewed side by side in this HTML report implmented with a CSS slider:  

(Note: Under testing for proper resource links.)  

[slider Report (html)]({{ site.url }}/_posts/sliderReport.html)


<a href="{{ site.url }}/_posts/sliderReport.html" target="_blank">slider Report</a>



[Github repo](https://github.com/CatChenal/Geocoders_Comparison)
