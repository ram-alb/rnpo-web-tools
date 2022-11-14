"""Views for network_vs_atoll app."""

from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv

from .src.excel import fill_excel
from .src.gsm.gsm_main import gsm_main
from .src.lte.lte_main import lte_main
from .src.summary import get_summary

load_dotenv('.env')

diffs = {}


def home(request):
    """
    View function for home page of network_vs_atoll app.

    Args:
        request: request object

    Returns:
        http response object
    """
    if request.method == 'GET':
        gsm_diffs = gsm_main()
        lte_diffs = lte_main()
        diffs['GSM'] = gsm_diffs
        diffs['LTE'] = lte_diffs
        context = get_summary(GSM=gsm_diffs, LTE=lte_diffs)
        return render(request, 'network_vs_atoll/home.html', context)

    if request.method == 'POST':
        technology = request.POST.get('technology')
        node = request.POST.get('node')

        report_path = fill_excel(technology, diffs[technology][node], node)
        with open(report_path, 'rb') as attachment:
            file_data = attachment.read()
            response = HttpResponse(file_data, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="network-vs-atoll.xlsx"'
            return response
