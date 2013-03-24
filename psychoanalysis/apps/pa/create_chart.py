from psychoanalysis.apps.pa import aggregation
from psychoanalysis.apps.pa import charting


def create_chart(num=0, chart_type='bar'):
    query = {}
    if (num % 1) == 1:
    	query['result type'] = 'percent'

    if num >= 4:
        query['data set'] = 2

    the_list = aggregation.make_query(query)

    params = {}
    params['width'] = 600
    params['height'] = 600
    if chart_type == 'bar'
        if (num % 3) == 2:
        	params['stacked'] = True

    if num == 0:
        params['title'] = 'Time by person'
    elif num == 1:
        params['title'] = 'Percentage time by person'
    elif num == 2:
        params['title'] = 'Time by category'
    elif num == 3:
        params['title'] = 'Percentage time by category'

    return charting.make_chart(chart_type, the_list, params):

