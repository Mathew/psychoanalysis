Charting and how to use it.

In your python file import charting

charting.make_chart takes three paramaters, chart type, a list and a dict.

The chart type is the type of chart you want. The current options are:
pie for a pie chart
bar for a bar chart. A bar chart can be made into columns by adding 'vertical': True to
the paramaters dict.
line for a line chart
The case of the type doesn't matter.

The list is a list of lists. The first item of the main list is a list of the names of
the fields you are plotting eg ['Lothians', 'Borders', 'Central', 'Highland'].
Each subsequent item is a list of the data name followed by one or more data points,
eg ['Pneumonia' 23, 34, 56, 67]. The first item must be a string and the rest integers
or floats.

The dict is a list of parameters you can use to specify your chart. The currently
defined ones are:
title, the title of the chart. If no title 'Chart' is used.
width, the width of the chart in pixels
height, the height of the chart in pixels
stacked, bar charts only and whether you want the bars stacked or not.

Tf you want a stacked bar graph called Diseases, 600 pixels wide and 500 pixels high, the
dict would be:
{'title': 'Diseases', 'width': 600, 'height': 500', 'stacked': True}

make_chart returns a string which goes into the <head>

To draw the chart include the line
<div id="chart_div" style="width: 90%; height: 90%;"></div>
in the place in the body you want the chart to appear.
