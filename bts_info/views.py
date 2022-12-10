"""Views for bts_info app."""

from django.contrib import messages
from django.shortcuts import render

from .forms import BtsIdForm
from .src.gsm.gsm_main import gsm_main
from .src.lte.lte_main import lte_main
from .src.wcdma.wcdma_main import wcdma_main


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
            gsm_site, gsm_sector_polygons = gsm_main(bts_id)
            lte_site, lte_sector_polygons = lte_main(bts_id)
            wcdma_site, wcdma_sector_polygons = wcdma_main(bts_id)
            sites = [*gsm_site, *wcdma_site, *lte_site]
            context = {
                'sites': sites,
                'form': BtsIdForm(),
                'sector_polygons': [
                    *gsm_sector_polygons,
                    *wcdma_sector_polygons,
                    *lte_sector_polygons,
                ],
            }
            if sites:
                context['latitude'] = sites[0]['latitude']
                context['longitude'] = sites[0]['longitude']
            else:
                messages.error(request, f'Site with id {bts_id} was not found')

            return render(request, 'bts_info/bts_info.html', context)

    form = BtsIdForm()
    return render(request, 'bts_info/bts_info.html', {'form': form})
