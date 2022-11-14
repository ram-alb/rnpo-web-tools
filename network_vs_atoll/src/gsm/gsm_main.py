"""Compare gsm parameters on the network wtih atoll parameters."""

from network_vs_atoll.src.gsm.compare import compare_gsm
from network_vs_atoll.src.gsm.gsm_select import (
    select_atoll_hsn,
    select_atoll_maio,
    select_cell_parameters,
)
from network_vs_atoll.src.gsm.parser import parse_hsn, parse_maio


def gsm_main():
    """
    Get gsm parameters diff.

    Returns:
        dict
    """
    cell_parameters = select_cell_parameters()
    atoll_hsn = select_atoll_hsn()
    atoll_maio = select_atoll_maio()
    hsns = parse_hsn(atoll_hsn)
    maios = parse_maio(atoll_maio)
    return compare_gsm(cell_parameters, hsns, maios)
