---
title: "Displaying images with a caption"
date: 2020-01-04
tags: [Data Visualization, HTML5]
excerpt: "Go figure..."
---

#### Unless an image already includes a caption, it is in many cases advisable to include one. 
#### Those familiar with HTML5 may know that there is a tag just for that!  

#### It's aptly named `<figure>`. Let's see how it works.

# Add an HTML image link with a caption with the `<figure>` tag wrapping the `<img>` tag:   
The next Markdown cell contains this HTML code:
```html
<figure style="display:inline-block; text-align:center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Sancerre_france.jpg/405px-Sancerre_france.jpg" 
       alt="x"
       style="display:block; width:600px; height:400px;"
       title="Sancerre, France"
   >
  <figcaption style="color:teal; font-weight:bold; font-family: Arial, Helvetica, sans-serif;">
       Figure 1 - A long view of Sancerre, France. Source: <a href="https://en.wikipedia.org/wiki/Sancerre">wikipedia</a>
  </figcaption>
</figure>
```

<figure style="display:inline-block; text-align:center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Sancerre_france.jpg/405px-Sancerre_france.jpg" 
       alt="x"
       style="display:block; width:600px; height:400px;"
       title="Sancerre, France">
  <figcaption style="color:teal; font-weight:bold; font-family: Arial, Helvetica, sans-serif;">
             Figure 1 - A long view of Sancerre, France. &ensp;Source: <a href="https://en.wikipedia.org/wiki/Sancerre">wikipedia</a>
  </figcaption>
</figure>

<div class="alert alert-info"><p style="font-size:1.2em"><b>Info: </b><br>&emsp;&emsp;* img.src can be local<br>&emsp;&emsp;* img.title attribute holds the tooltip text</p></div>

<figure style="display:inline-block; text-align:center">
  <img src="{{ site.url }}/assets/images/Finley.JPG" 
       alt="x"
       style="display:block; width:500px; height:400px;"
       title="John Finley Walk">
  <figcaption style="color:teal; font-weight:bold; font-family: Arial, Helvetica, sans-serif;">
             Figure 2 (local) - <a href="https://en.wikipedia.org/wiki/John_Huston_Finley">John Finley</a>
  </figcaption>
</figure>

