"""Compare parameters from the network with atoll parameters."""


def create_diff(row, parameter, network_value, atoll_value):
    """
    Make diff for one parameter.

    Args:
        row: namedtuple
        parameter: string
        network_value: string or number
        atoll_value: string or number or None
    """
    return {
        'subnetwrok': row.subnetwork,
        'site': row.sitename,
        'cell': row.eutrancell,
        'parameter': parameter,
        'network_value': network_value,
        'atoll_value': atoll_value,
    }


def compare_parameter(diff, row, parameter_name, atoll_value):
    """
    Compare one parameter and add it to diff if network value is not equal to atoll value.

    Args:
        diff: list
        row: namedtuple
        parameter_name: string
        atoll_value: string or number or None
    """
    row_as_dict = row._asdict()
    if row_as_dict[parameter_name] != atoll_value:
        diff.append(create_diff(
            row,
            parameter_name,
            row_as_dict[parameter_name],
            atoll_value,
        ))


def compare(selected_network_cells, atoll_cells):
    """
    Compare parameters from the network with atoll parameters.

    Args:
        selected_network_cells: cx-Oracle fetchall object
        atoll_cells: dict

    Returns:
        dict
    """
    diff = {}
    for row in selected_network_cells:
        subnetwork = row.subnetwork
        cell_name = row.eutrancell
        try:
            atoll_cell = atoll_cells[cell_name]
        except KeyError:
            continue
        if subnetwork not in diff.keys():
            diff[subnetwork] = []
        compare_parameter(diff[subnetwork], row, 'sitename', atoll_cell['sitename'])
        compare_parameter(diff[subnetwork], row, 'tac', atoll_cell['tac'])
        compare_parameter(diff[subnetwork], row, 'cellid', atoll_cell['cellid'])
        compare_parameter(diff[subnetwork], row, 'pci', atoll_cell['pci'])
        compare_parameter(diff[subnetwork], row, 'earfcndl', atoll_cell['earfcndl'])
        compare_parameter(diff[subnetwork], row, 'rach', atoll_cell['rach'])
    return diff
