"""Prepare WCDMA site data."""

from ..handler import handle_atoll_data
from ..sector_polygons import make_sector_polygons
from .wcdma_select import make_wcdma_atoll


def wcdma_main(site_id):
    """
    Prepare WCDMA site data.

    Args:
        site_id (str): 5 digits string

    Returns:
        list: a list of dicts with WCDMA cells data
    """
    wcdma_atoll = make_wcdma_atoll(site_id)
    atoll_wcdma_data = wcdma_atoll.execute_sql_command('select_wcdma_site')
    site_data = handle_atoll_data(atoll_wcdma_data)
    sector_polygons = make_sector_polygons(atoll_wcdma_data, 'WCDMA')
    return (site_data, sector_polygons)
