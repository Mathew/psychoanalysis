import os
import traceback
import sys

def make_chart(chart_type, data_list, params):
    chart_type = chart_type.lower()
    ret_str = ''
    if chart_type == 'pie':
        ret_str = make_pie(data_list, params)
    elif chart_type == 'bar':
        ret_str = make_bar(data_list, params)
    elif chart_type == 'line':
        ret_str = make_line(data_list, params)

    ret_str += 'chart.draw(data, options);\r\n}\r\n</script>\r\n'

    return ret_str


def make_line(data_list, params):
    ret_str = make_data_block(data_list, params)

    ret_str += "var chart = new google.visualization.LineChart(document.getElementById('chart_div'));\r\n"
    return ret_str


def make_bar(data_list, params):
    ret_str = make_data_block(data_list, params)

    if 'vertical' in params:
        ret_str += "var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));\r\n"
    else:
        ret_str += "var chart = new google.visualization.BarChart(document.getElementById('chart_div'));\r\n"

    return ret_str


def make_pie(data_list, params):
    ret_str = make_data_block(data_list, params)

    ret_str += "var chart = new google.visualization.PieChart(document.getElementById('chart_div'));\r\n"
    return ret_str


def make_data_block(data_list, params):
    num = 0
    ret_str = get_head_start()
    for row in data_list:
        col = 0
        the_str = ''
        for item in row:
            if col == 0:
            	the_str += "['{0}'".format(item)
            else:
            	if num == 0:
            		the_str += ", '{0}'".format(item)
            	else:
            		the_str += ", {0}".format(item)
            col += 1

        if len(the_str):
            the_str += ']'
            if num > 0:
                ret_str += ',\r\n'
            ret_str += the_str
            num += 1

    ret_str += '\r\n]);\r\n'
    ret_str += build_options(params)

    return ret_str


def get_string(the_item):
	the_key = the_item.iterkeys().next()
	the_val = the_item.itervalues().next()
	return "['{0}', '{1}']".format(the_key, the_val)


def get_float(the_item):
	the_key = the_item.iterkeys().next()
	the_val = the_item.itervalues().next()
	return "['{0}', {1}]".format(the_key, the_val)


def get_head_start():
    ret_str = '<script type="text/javascript" src="https://www.google.com/jsapi"></script>\r\n'
    ret_str += '<script type="text/javascript">\r\n'
    ret_str += "google.load(\"visualization\", \"1\", {packages:[\"corechart\"]});\r\n"
    ret_str += 'google.setOnLoadCallback(drawChart);\r\n'
    ret_str += 'function drawChart() {\r\n'
    ret_str += 'var data = google.visualization.arrayToDataTable([\r\n'

    return ret_str


def build_options(the_options):
    ret_str = 'var options = {\r\ntitle: "'
    if 'title' in the_options:
        ret_str += the_options['title']
    else:
        ret_str +=  'Chart'
    ret_str +=  '",\r\n'

    if 'width' in the_options:
        ret_str += 'width: {0},\r\n'.format(the_options['width'])

    if 'height' in the_options:
        ret_str += 'height: {0},\r\n'.format(the_options['height'])

    if 'stacked' in the_options:
        ret_str += 'isStacked: true,\r\n'

    ret_str += '};\r\n'

    return ret_str
