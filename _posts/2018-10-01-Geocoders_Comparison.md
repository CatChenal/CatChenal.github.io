---
title: "Geocoders Comparison"
date: 2018-10-01
tags: [Data Visualization, GIS, folium]
excerpt: "Discovering the geocoding quirks &mdash; a polite characterization&mdash; in Nominatim, GoogleV3, ArcGis and AzureMaps APIs."
---

# Comparison of four geocoders: Nominatim, GoogleV3, ArcGis and AzureMaps


## Which is the best geocoder?

Although I do not no what the gound truth is - apart from the fact that I compared only four geocoders out of the 47 available via geopy-
The worse of the four I compared is Azure maps: getting 'Richmond Hill, New York' while the query was 'Richmond county New York, NY, USA' (see panel H) , or
some location in Long Island for the query 'Kings county, New York, NY, USA' (see panel H) is, IMHO, inadmissible.
Next is ArcGis, which usually returns oversize boxes, except for Brooklyn where its box is too short (even ignoring the maritime area).
Nominatim and GoogleV3 have similar results, but Nominatim is free.


So, yes, Nominatim wins!

[Github repo:](https://github.com/CatChenal/Geocoders_Comparison)

[HTML report](/assets/images/GeocodersComparisonReport.html)

