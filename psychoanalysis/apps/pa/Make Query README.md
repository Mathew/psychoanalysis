To get a data set and create a chart call make_query in create_chart.py with two parameters.
First parameter is an integer between 0 and 8 for one of the four data sets.
The second parameter is the chart type. It can be 'bar', 'pie' or 'line' Bar charts with a number greater than 3 will produce a column chart.

make_query returns a string which must go somewhere in the head. It loads a javascript libray and google charts.

In the <body> the line:
<div id="chart_div" style="width: 90%; height: 90%;"></div>

should go where you want the chart to appear.
