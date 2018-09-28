---
title: "How to label a matplotlib bar plot"
date: 2018-07-11
tags: [Data Visulaization]
excerpt: "Fine tuning a Matplotlib barplot"
---

# How to label a matplotlib bar plot
(Hint: never (re)iterate the data source, use the plot objects)

At some point during EDA, you often produce summary tables (after an untold number of processing steps), which can be nicely visualized with a bar plot.

**Here, I show how to modify the default output for a more appealing result.**

[abbreviated file for debugging]

# Code:

```python
import matplotlib.pyplot as plt
%matplotlib inline

from IPython.display import display, Image

import numpy as np
import pandas as pd
pd.set_option('precision', 2)
np.set_printoptions(precision=2)
```

### For EDA, you often produce summary tables (after an untold number of processing steps).  
### The summary table for categorical responses to a survey may look like this:
# Raw data:
,Very interested,Somewhat interested,Not interested
Data Analysis,0.77,0.2,0.03
Machine Learning,0.75,0.22,0.03
Data Vis.,0.62,0.34,0.05
Big Data,0.61,0.33,0.06
Deep Learning,0.58,0.36,0.06
Data Journalism,0.2,0.51,0.29

```python
df = pd.read_csv('./data/ordered_survey_pct.csv', header=0, 
                 names=['Very interested', 'Somewhat interested', 'Not interested'])
df
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Very interested</th>
      <th>Somewhat interested</th>
      <th>Not interested</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Data Analysis</th>
      <td>0.77</td>
      <td>0.20</td>
      <td>0.03</td>
    </tr>
    <tr>
      <th>Machine Learning</th>
      <td>0.75</td>
      <td>0.22</td>
      <td>0.03</td>
    </tr>
    <tr>
      <th>Data Vis.</th>
      <td>0.62</td>
      <td>0.34</td>
      <td>0.05</td>
    </tr>
    <tr>
      <th>Big Data</th>
      <td>0.61</td>
      <td>0.33</td>
      <td>0.06</td>
    </tr>
    <tr>
      <th>Deep Learning</th>
      <td>0.58</td>
      <td>0.36</td>
      <td>0.06</td>
    </tr>
    <tr>
      <th>Data Journalism</th>
      <td>0.20</td>
      <td>0.51</td>
      <td>0.29</td>
    </tr>
  </tbody>
</table>
</div>



## With this kind of data in a pandas dataframe, the typical visualization is a bar plot, which is produced using pandas plotting function:

> <span style="font-size:2em; color:darkblue;"> DataFrame.plot( kind='bar' , ...) </span>


## Default output after specifying the bars color, figure size & title:


```python
colors = ['#5cb85c', '#5bc0de', '#d9534f']
ax = df.plot(kind='bar', color=colors, alpha=0.8, width=0.8, 
             figsize=(12, 6), fontsize=14,
             title="Percentage of Respondents' interest in Data Science Areas")

plt.savefig('../assets/images/barplot_First_output.png', format='png', layout='tight')
plt.tight_layout();
```

![png]('../assets/images/barplot_First_output.png')


## By default:
 -  <span style="font-size:2em; ">the y-axis is visible </span>
 -  <span style="font-size:2em; ">the plot frames, called __spines__, are visible </span>
 -  <span style="font-size:2em; ">the legend is placed in the upper right corner </span>


## Because the bar heights equal the values in the series, the y-axis is redundant and a more desirable output would be this one:  
![png]("../assets/images/Bar_plot_Percentage_of_Respondents.png")


# Anatomy of a bar plot via its *containers* collection:  

## Containers are defined for each data series. They have 2 attributes:  
> <span style=" font-size:2em;">__Attributes:__ </span>
>> <span style=" font-size:2em;"><span style="color:darkblue;">patches</span>: list of Rectangle objects. </span>  
    <span style=" font-size:1em;">The artists of the bars. </span>

>> <span style=" font-size:2em;">errorbar: None or ErrorbarContainer. </span>  
    <span style=" font-size:1em;">A container for the error bar artists if error bars are present. None otherwise.  </span>
   


```python
print('Categories in df: {}\n'.format(df.index.size) )

for c in ax.containers:
    print(c.get_label(), '\t', len(c.patches))
```

    Categories in df: 6
    
    Very interested 	 6
    Somewhat interested 	 6
    Not interested 	 6
    

# In the matplotlib object model, the bars, or rectangles, of a bar plot belong to the patches collection. You can access their values using the patches collection of an axis via the associated
><span style="font-size:2em; color:darkblue">*.get_...()* methods: </span>


```python
for p in ax.patches:
    p_x = round(p.get_xy()[0], 2)
    p_h = round(p.get_height(), 2)
    
    print('p_x: {}, p_h: {}'.format(p_x, p_h)) 
```

    p_x: -0.4, p_h: 0.77
    p_x: 0.6, p_h: 0.75
    p_x: 1.6, p_h: 0.62
    p_x: 2.6, p_h: 0.61
    p_x: 3.6, p_h: 0.58
    p_x: 4.6, p_h: 0.2
    p_x: -0.13, p_h: 0.2
    p_x: 0.87, p_h: 0.22
    p_x: 1.87, p_h: 0.34
    p_x: 2.87, p_h: 0.33
    p_x: 3.87, p_h: 0.36
    p_x: 4.87, p_h: 0.51
    p_x: 0.13, p_h: 0.03
    p_x: 1.13, p_h: 0.03
    p_x: 2.13, p_h: 0.05
    p_x: 3.13, p_h: 0.06
    p_x: 4.13, p_h: 0.06
    p_x: 5.13, p_h: 0.29
    

# How to label the bars?  
><span style="font-size:2em; color:darkblue">*axis.text()* method: </span>


```python
plt.close('all');

colors = ['#5cb85c', '#5bc0de', '#d9534f']

ax = df.plot(kind='bar', 
             color=colors, 
             alpha=0.8, 
             figsize=(12, 6), 
             fontsize=14);

ax.spines['left'].set_visible(False);
ax.spines['top'].set_visible(False);
ax.spines['right'].set_visible(False);
ax.spines['bottom'].set_color('#CCCCCC');

# Adjust vertical limits to 100% to get more whitespace below the title:
plt.ylim(0, 1)

# Remove axes tick marks:
plt.yticks([]); # remove both ticks and labels on y-axis
plt.tick_params(axis='x', which='major', bottom=False) # remove ticks only

# Annotate Text 
x_offset = 0.00  # (bar_width/len(df.columns))/2  #:: mid bar width
y_offset = 0.03

for p in ax.patches:
    p_x = p.get_xy()[0]
    p_h = p.get_height()
    ax.text( x=p_x + x_offset, y=p_h + y_offset , s="{:.0f}%".format(round(p_h*100, 0)), 
             ha='left', va='center', fontsize=11)
        
# NOTE: ha='left' goes with x_offset = 0. If instead ha='center',
#       the label will 'pre-hang' over the bar, so an x-position offset will be needed.       
    
# Reset font size from smaller default:
plt.legend(fontsize=14);

plt.title("Percentage of Respondents' interest in Data Science Areas", fontsize=16);

plt.savefig('../assets/images/barplot_Final_output.png', format='png', transparent=True, layout='tight')
plt.tight_layout();
```

![png]('../assets/images/barplot_Final_output.png')
