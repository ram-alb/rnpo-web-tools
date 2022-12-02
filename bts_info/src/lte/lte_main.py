"""Prepare LTE site data."""

from .lte_enm import make_lte_enm_cli
from .lte_select import make_lte_atoll
from .parser_funcs import parse_mimo_order, unite_atoll_enm_data


def lte_main(site_id):
    """
    Prepare LTE site data.

    Args:
        site_id (str): 5 digits string

    Returns:
        list: a list of dicts with LTE cells data

    """
    lte_enm_cli = make_lte_enm_cli(site_id)
    enm_tx_data = lte_enm_cli.execute_cmedit_get_command('SectorCarrier')
    mimo_order = parse_mimo_order(enm_tx_data)

    lte_atoll = make_lte_atoll(site_id)
    atoll_lte_site = lte_atoll.execute_sql_command('select_lte_site')
    return unite_atoll_enm_data(atoll_lte_site, mimo_order)
