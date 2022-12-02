"""Parse lte data."""

from utils.enm_parser_utils import parse_mo_value


def parse_cell_name(reserved_by_val):
    """
    Parse cell name from SectorCarrier.reservedBy parameter value.

    Args:
        reserved_by_val (str): SectorCarrier.reservedBy parameter value

    Returns:
        str or None
    """
    try:
        cell_name = parse_mo_value(reserved_by_val, 'EUtranCellFDD')
    except AttributeError:
        cell_name = None
    return cell_name


def parse_mimo_order(enm_tx_data):
    """
    Parse MIMO order by number of tx antennas.

    Args:
        enm_tx_data (enmscripting ElementGroup object): result of
            enm cli command

    Returns:
        dict: cell_name is a key, MIMO order is a value
    """
    mimo_order = {}
    mimo_types = {
        '0': 'no MIMO',
        '1': 'no MIMO',
        '2': 'MIMO 2*2',
        '4': 'MIMO 4*4',
    }
    for element in enm_tx_data:
        element_value = element.value()
        if ' : ' in element_value:
            parameter_name, parameter_value = element_value.split(' : ')
            if parameter_name == 'noOfTxAntennas':
                tx_number = parameter_value
            elif parameter_name == 'reservedBy':
                cell_name = parse_cell_name(parameter_value)
                mimo_order[cell_name] = mimo_types[tx_number]
    return mimo_order


def unite_atoll_enm_data(atoll_data, mimo_order):
    """
    Unite atoll data and enm data.

    Args:
        atoll_data (list): a list of namedtuples with lte cells
        mimo_order (dict): a cell_name is a key, MIMO order is a value

    Returns:
        list: a list of dicts with united atoll and enm data
    """
    lte_site_data = []

    for row in atoll_data:
        cell_name = row.cell
        try:
            mimo = mimo_order[cell_name]
        except KeyError:
            mimo = None
        row = row._replace(longitude=round(row.longitude, 5))
        row = row._replace(latitude=round(row.latitude, 5))
        lte_site_data.append({**row._asdict(), 'MIMO': mimo})

    return lte_site_data
