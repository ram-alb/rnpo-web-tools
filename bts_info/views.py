"""Views for bts_info app."""

from django.contrib import messages
from django.shortcuts import render

from .forms import BtsIdForm
from .src.lte.lte_main import lte_main


def bts_info(request):
    """
    Display site data or form for requesting site depending on method.

    Args:
        request: http request object

    Returns:
        http response object
    """
    if request.method == 'POST':
        form = BtsIdForm(request.POST)
        if form.is_valid():
            bts_id = form.cleaned_data['bts_id']
            sites = lte_main(bts_id)
            if not sites:
                messages.error(request, f'Site with id {bts_id} was not found')
            return render(request, 'bts_info/bts_info.html', {'sites': sites, 'form': BtsIdForm()})

    form = BtsIdForm()
    return render(request, 'bts_info/bts_info.html', {'form': form})
