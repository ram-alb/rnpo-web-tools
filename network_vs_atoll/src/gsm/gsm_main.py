"""Compare gsm parameters on the network wtih atoll parameters."""

from dotenv import load_dotenv
from network_vs_atoll.src.gsm.compare import compare_gsm
from network_vs_atoll.src.gsm.gsm_select import (
    select_atoll_hsn,
    select_atoll_maio,
    select_cell_parameters,
)
from network_vs_atoll.src.gsm.parser import parse_hsn, parse_maio

load_dotenv('.env')


def get_gsm_diff():
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
    diff = compare_gsm(cell_parameters, hsns, maios)
    return diff


def gsm_main():
    """
    Prepare gsm diff data for network_vs_atoll app.

    Returns:
        tuple
    """
    gsm_diff = get_gsm_diff()
    inconsistencies_count = 0
    summary_by_bsc = []

    for bsc, cells in gsm_diff.items():
        bsc_inconsistencies_count = len(cells)
        inconsistencies_count += bsc_inconsistencies_count
        summary_by_bsc.append({
            'bsc_name': bsc,
            'count': bsc_inconsistencies_count,
        })

    return (inconsistencies_count, summary_by_bsc, gsm_diff)
