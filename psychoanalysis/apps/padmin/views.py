from psychoanalysis.apps.pa.create_chart import create_chart
from django.shortcuts import render


def chart_view(request, data=1, chart_type='bar'):
    print data
    print chart_type

    head = create_chart(int(data), chart_type)

    return render(request, 'padmin/admin_index.html', {
        'chart_head': head,
    })
