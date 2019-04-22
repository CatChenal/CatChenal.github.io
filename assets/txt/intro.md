## Comparison of Four Geocoders: Nominatim, GoogleV3, ArcGis and AzureMaps

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
I used two shapefiles: that of New York City (with water extent), and that of Boston, without water extent as it was the only one I found.<br>
* New York City: https://data.cityofnewyork.us/City-Government/Borough-Boundaries-Water-Areas-Included-/tv64-9x69<br>
* Boston: https://data.boston.gov/dataset/city-of-boston-boundary2<br>

### Places queried:
* "New York City, NY, USA"<br>
* "Cleopatra's needle, Central Park, New York, NY, USA"<br>
* "Bronx county, NY, USA"<br>
* "Kings county, NY, USA"<br>
* "New York county, NY, USA"<br>
* "Queens county, NY, USA"<br>
* "Richmond county, NY, USA"<br>
* "Boston, MA, USA"<br>

### Update: Report on temporal differences:  
Because I noticed that the results from this April were different from those from last September (2018), I put together an HTML report highlighting the differences.  A persistent oddity is that half of the geocoders tested cannot distinguish between "New York City" and "New York county" (Manhattan): GoogleV3 and ArcGis return identical bounding boxes.

### Slides in this updated report:   
1. Intro (this slide)  
**Heatmaps of pairwise distance differences:**  
-> How large are the distance differences for each geocoder in this comparison?
2. Old heatmaps
3. New heatmaps  
**Relationship between center of bounding box and queried location (NYC):**  
4. Comparison tables  
**Maps:**  
5. New York City
6. New York county (Manhattan)
7. Cleopatra's Needle (a monument in Central Park)
8. Bronx county
9. Brooklyn county
10. Queens county
11. Richmond county (Staten Island)
12. Boston

### The main conclusions from this comparison:
**Which is the best of these four?**  
1. **Nominatim**: &#x2B50; of the glorious open-source community that is OpenStreetMap;  
2. **GoogleV3**: similar results to Nominatim; requires an account;  
3. ArcGis: the least wrong of the worse two  
4. AzureMaps: Oh come on! &#128534;

**No hedging!**  
I presume that it is very unlikely that an application would use different geolocating services, but in the case some 'hedging' is involved (e.g. on limits, time-outs), the geolocation for the same query will be different.

**Mind the box!**  
Additionally, my non-exhaustive comparison of four Geopy geocoders (out of 21), reveals that the boxing of a location is not always principled. For instance, Nominatim and GoogleV3 most often use the shapefile with water extent for boxing, whereas ArcGis and AzureMaps do not; moreover, ArcGis boxes typically extend further North than warranted by the existing shapefiles by at most 10 miles.    

#### Final notes on accuracy in the geolocation context:

I found this [excellent resource](https://gis.stackexchange.com/questions/8650/measuring-accuracy-of-latitude-and-longitude) on precision for geolocations. Here are the main points:  

<table>
  <tr>
    <th id=col2>Decimal place (ordinal)</th> 
    <th id=col2>Maximal resolved distance</th><th id=col3>Comments on precision</th>
  </tr>
  <tr>
    <td id=col1>1</td> <td id=col2>11.1 km</td>
    <td id=col3>can distinguish the position of one large city from a neighboring large city</td>
  </tr>
  <tr>
    <td id=col1>2</td> <td id=col2>1.1 km </td>
    <td id=col3>can separate one village from the next</td>
  </tr>
  <tr>
    <td id=col1>3</td> <td id=col2>110 m</td>
    <td id=col3>can identify a large agricultural field or institutional campus</td>
  </tr>
  <tr>
    <td id=col1>4</td> <td id=col2>11 m</td>
    <td id=col3>can identify a parcel of land. It is comparable to the typical accuracy of an uncorrected GPS unit with no interference</td>
  </tr>
  <tr>
    <td id=col1>5</td> <td id=col2>1.1 m</td>
    <td id=col3>can distinguish trees from each other. Accuracy to this level with commercial GPS units can only be achieved with differential correction</td>
  </tr>
  <tr>
    <td id=col1>6</td> <td id=col2>0.11 m</td>
    <td id=col3>can be used for laying out structures in detail, for designing landscapes, building roads. It should be more than good enough for tracking movements of glaciers and rivers. This can be achieved by taking painstaking measures with GPS, such as differentially corrected GPS</td>
  </tr>
  <tr>
    <td id=col1>7</td> <td id=col2>11 mm</td>
    <td id=col3>good for surveying and is near the limit of what GPS-based techniques can achieve</td>
  </tr>
  <tr>
    <td id=col1>8</td> <td id=col2>1.1 mm</td>
    <td id=col3>good for charting motions of tectonic plates and movements of volcanoes. Permanent, corrected, constantly-running GPS base stations might be able to achieve this level of accuracy</td>
  </tr>
  <tr>
    <td id=col1>9</td> <td id=col2>110 microns</td>
    <td id=col3>we are getting into the range of microscopy. For almost any conceivable application with earth positions, this is overkill and will be more precise than the accuracy of any surveying device</td>
  </tr>
  <tr>
     <td id=col1>> 9</td> <td id=col1>useless</td> 
     <td id=col3>indicates a computer or calculator was used and that no attention was paid to the fact that the extra decimals are useless. Be careful, because unless you are the one reading these numbers off the device, this can indicate low quality processing!</td>
  </tr>
</table>
