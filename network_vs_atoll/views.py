"""Views for network_vs_atoll app."""

from django.http import HttpResponse
from django.shortcuts import render

from .src.gsm.excel import fill_excel
from .src.gsm.gsm_main import gsm_main
from .src.lte.lte_main import lte_main


def home(request):
    """
    View function for home page of network_vs_atoll app.

    Args:
        request: request object

    Returns:
        http response object
    """

    diffs = {
        'summary': [],
    }
    gsm_inconsistencies_count, summary_by_bsc, gsm_diff = gsm_main()
    lte_inconsistencies_count, summary_by_subnetworks, lte_diff = lte_main()
    diffs['summary'].append({
        'technology': 'GSM',
        'count': gsm_inconsistencies_count,
    })
    diffs['summary'].append({
        'technology': 'LTE',
        'count': lte_inconsistencies_count,
    })
    diffs['gsm_details'] = summary_by_bsc
    diffs['lte_details'] = summary_by_subnetworks

    if request.method == 'POST':
        bsc_name = request.POST.get('bsc')
        report_path = fill_excel(gsm_diff, bsc_name)
        with open(report_path, 'rb') as attachment:
            file_data = attachment.read()
            response = HttpResponse(file_data, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="network-vs-atoll.xlsx"'
            return response

    return render(request, 'network_vs_atoll/home.html', diffs)
