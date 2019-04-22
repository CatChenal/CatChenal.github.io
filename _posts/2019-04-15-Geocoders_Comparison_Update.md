---
title: "Geocoders Comparison Update"
date: 2019-04-15
tags: [Data Visualization, GIS, folium]
excerpt: "Discovering the geocoding quirks in Nominatim, GoogleV3, ArcGis and AzureMaps APIs: September, 2018 vs. April, 2019 results."
---

# Comparison of four geocoders: Nominatim, GoogleV3, ArcGis and AzureMaps

### Geocoding services (via Geopy):
Geocoding refers to the maping of an address to its geographic coordinates. Specifically, the geocoding of a location specified by a query string can be achieved using calls to geocoding services (APIs) directly in a browser address box, or with a wrapping library such as [Geopy](https://geopy.readthedocs.io/en/stable/).

### Why I setup this comparison:
In another application, I tried using the New York City boroughs bounding boxes to impute missing borough names for records with geolocation information (via set operations) as a way to prevent over 85,000 requests. I trashed the box 'solution' once I found out about the official territorial boundaries (shapefiles). Yet, in the intervening time I had checked several services for speed and limits and I found that some geocoders were not returning the same geolocation or bounding boxes for the same query, so I investigated!

To date, April 2019, Geopy has 21 traditional geocoders (excluding What3Words), so I picked only four of them. Following are the links to the geocoders documentation and their respective service providers via Geopy: 
<ul>
    <li><a href="https://geopy.readthedocs.io/en/stable/#nominatim"><strong>Nominatim: </strong></a> 
        <a href="https://wiki.openstreetmap.org/wiki/Using_OpenStreetMap">OpenStreetMaps</a>
    </li>
    <li>
        <a href="https://geopy.readthedocs.io/en/stable/#googlev3"><strong>GoogleV3: </strong></a>
        <a href="https://developers.google.com/maps/documentation/geocoding/start">Google Map & Places API</a>
    </li>
    <li>
        <a href="https://geopy.readthedocs.io/en/stable/#ArcGis"><strong>ArcGis: </strong></a>
        <a href="https://developers.arcgis.com/rest/geocode/api-reference/overview-world-geocoding-service.htm">ESRI ArcGIS API</a>
    </li>
    <li>
        <a href="https://geopy.readthedocs.io/en/stable/#azuremaps"><strong>AzureMaps: </strong></a>
        <a href="https://docs.microsoft.com/en-us/azure/azure-maps/index">Microsoft Azure Maps API</a>
    </li>
</ul>

### Shapefile sources:
I used two shapefiles: that of New York City (with water extent), and that of Boston, without water extent as it was the only one I found.  
* New York City: https://data.cityofnewyork.us/City-Government/Borough-Boundaries-Water-Areas-Included-/tv64-9x69  
* Boston: https://data.boston.gov/dataset/city-of-boston-boundary2  

### Places queried:
* "New York City, NY, USA"  
* "Cleopatra's needle, Central Park, New York, NY, USA"  
* "Bronx county, NY, USA"  
* "Kings county, NY, USA"  
* "New York county, NY, USA"  
* "Queens county, NY, USA"  
* "Richmond county, NY, USA"  
* "Boston, MA, USA"  

### Update: Report on temporal differences:  
Because I noticed that the results from this April were different from those from last September (2018), I put together an HTML report highlighting the differences.  A persistent oddity is that half of the geocoders tested cannot distinguish between "New York City" and "New York county" (Manhattan): GoogleV3 and ArcGis return identical bounding boxes.

The older and newer results are displayed in an HTML report implemented with a CSS slider: 
<a href="{{ site.url }}/assets/sliderReport.html" target="_blank">slider Report</a>

I've implemented the report by modifying a ["JS-less CSS slider"](https://github.com/drygiel/csslider) designed by GH user drygiel.Thank you, drygiel!

In my GitHub repo, the [**Procedures notebook**](https://github.com/CatChenal/Geocoders_Comparison/notebooks/Procedures.ipnyb) details the processing steps and the production of tables and maps included in the slider report.

# The main conclusion from this comparison:  
I presume that it is very unlikely that an application would use different geolocating services, but in the case some 'hedging' is involved (e.g. on limits, time-outs), the geolocation for the same query will be different.
Additionally, my non-exhaustive comparison of four Geopy geocoders (out of 21), reveals that the boxing of a location is not always principled. For instance, Nominatim and GoogleV3 most often use the shapefile with water extent for boxing, whereas ArcGis and AzureMaps do not; moreover, ArcGis boxes typically extend further North than warranted by the existing shapefiles by at most 10 miles.  


[Github repo](https://github.com/CatChenal/Geocoders_Comparison)
