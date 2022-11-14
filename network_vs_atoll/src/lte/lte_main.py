"""Compare lte parameters on the network wtih atoll parameters."""

from .compare import compare
from .lte_select import select_atoll_cells, select_network_live_cells
from .parser import parse_atoll_cells


def lte_main():
    """
    Get lte parameters diff.

    Returns:
        dict
    """
    selected_atoll_cells = select_atoll_cells()
    atoll_cells = parse_atoll_cells(selected_atoll_cells)

    selected_network_cells = select_network_live_cells()
    return compare(selected_network_cells, atoll_cells)
