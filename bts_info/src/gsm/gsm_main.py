"""Prepare GSM site data."""

from ..handler import handle_atoll_data
from ..sector_polygons import make_sector_polygons
from .gsm_select import make_gsm_atoll


def gsm_main(site_id):
    """
    Prepare GSM site data.

    Args:
        site_id (str): 5 digits string

    Returns:
        list: a list of dicts with GSM cells data
    """
    gsm_atoll = make_gsm_atoll(site_id)
    atoll_gsm_data = gsm_atoll.execute_sql_command('select_gsm_site')
    site_data = handle_atoll_data(atoll_gsm_data)
    sector_polygons = make_sector_polygons(atoll_gsm_data, 'GSM')
    return (site_data, sector_polygons)
