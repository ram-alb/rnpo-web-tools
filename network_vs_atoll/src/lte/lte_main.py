"""Compare lte parameters on the network wtih atoll parameters."""

from .lte_select import select_atoll_cells, select_network_live_cells
from .parser import parse_atoll_cells
from .compare import compare


def lte_main():
    selected_atoll_cells = select_atoll_cells()
    atoll_cells = parse_atoll_cells(selected_atoll_cells)

    selected_network_cells = select_network_live_cells()
    diff = compare(selected_network_cells, atoll_cells)

    inconsistencies_count = 0
    summary_by_subnetworks = []

    for subnetwork, cells in diff.items():
        subnetwork_inconsistencies_count = len(cells)
        inconsistencies_count += subnetwork_inconsistencies_count
        summary_by_subnetworks.append({
            'subnetwork': subnetwork,
            'count': subnetwork_inconsistencies_count,
        })

    return (inconsistencies_count, summary_by_subnetworks, diff)
